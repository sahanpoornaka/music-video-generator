import sys
import os
import glob

import pickle
import librosa
import numpy as np

from modules import similarity

# Set Directories
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
sys.path.append(ROOT_DIR)

FILE_PATH = "/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/src/resources/pred/as-deka-wage-hitiya.MP3"
INITIAL_LEN = 1.0

INDEX_PATH = "/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/src/db/index"
META_PATH = "/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/src/db/meta"

RESTRICTED_CLIPS = []
def func_1(filepath, offset, duration):
    y, sr = librosa.load(filepath, offset=offset, duration=duration)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    # this is the number of samples in a window per fft
    n_fft = 2048
    # The amount of samples we are shifting after each fft
    hop_length = 512

    mel_signal = librosa.feature.melspectrogram(y=y, sr=sr, hop_length=hop_length, 
    n_fft=n_fft)
    spectrogram = np.abs(mel_signal)
    power_to_db = librosa.power_to_db(spectrogram, ref=np.max)

    similarities = []
    file_names = glob.glob(INDEX_PATH+"/*.npy")
    file_names = list(set(file_names) - set(RESTRICTED_CLIPS))
    for idx_file in file_names:
        idx_mtx = np.load(idx_file)
        dist = similarity.calculate_cosine_distance(idx_mtx, power_to_db)
        similarities.append(dist)

    min_index = similarities.index(min(similarities))
    sim_aud_file = file_names[min_index]

    with open(META_PATH+"/"+sim_aud_file.split("/")[-1].split(".")[0]+".pkl", 'rb') as f:
        audio_info = pickle.load(f)

    return [sim_aud_file, audio_info['length']]

aud_len = 0.0
gen_clips = []
gen_lengths = []
for idx in range (20):
    [aud_file_name, aud_len] = func_1(FILE_PATH, 0.0+aud_len, INITIAL_LEN)
    RESTRICTED_CLIPS.append(aud_file_name)
    gen_clips.append(aud_file_name)
    gen_lengths.append(aud_len)
# [aud_file_name, aud_len] = func_1(FILE_PATH, 0.0, INITIAL_LEN)
# print(aud_file_name, aud_len)
# [aud_file_name, aud_len] = func_1(FILE_PATH, 0.0+aud_len, INITIAL_LEN)
# print(aud_file_name, aud_len)


# Concat Video Clips
from moviepy.editor import *
 

clips = []
for clip in gen_clips:
    mp4_filename = clip.split("/")[-1].split(".")[0]
    clips.append(VideoFileClip(META_PATH+"/"+mp4_filename+".mp4"))

# concatenating both the clips
final_videoclip = concatenate_videoclips(clips)

final_audioclip = AudioFileClip(FILE_PATH).subclip(0, sum(gen_lengths))

videoclip = final_videoclip.set_audio(final_audioclip)
#writing the video into a file / saving the combined video
videoclip.write_videofile("/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/src/tmp/merged.mp4")


# print(gen_clips)
# print(gen_lengths)