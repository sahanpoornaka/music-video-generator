import os
import glob
import librosa
import numpy as np
import pickle

# from pydub import AudioSegment

# AUDIO_CLIP_LENGTH = 2

# def clip_audio(audio_list, output_path):
#     for audio in audio_list:
#         audio_seg = AudioSegment.from_file(audio)
#         audio_filename = os.path.basename(audio).split(".")[0]
#         audio_len = len(audio_seg)
#         clipped = audio_seg[(audio_len - AUDIO_CLIP_LENGTH)/2: (audio_len + AUDIO_CLIP_LENGTH)/2]
#         clipped.export(output_path + "/" + audio_filename + "_clipped.mp3", format="mp3")

INDEX_PATH = "/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/src/db/index"
META_PATH = "/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/src/db/meta"

def generate_mel_diagram(audio_file_path, audio_length, file_name):
    # Load Audio File
    y, sr = librosa.load(audio_file_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    # this is the number of samples in a window per fft
    n_fft = 2048
    # The amount of samples we are shifting after each fft
    hop_length = 512

    mel_signal = librosa.feature.melspectrogram(y=y, sr=sr, hop_length=hop_length, 
    n_fft=n_fft)
    spectrogram = np.abs(mel_signal)
    power_to_db = librosa.power_to_db(spectrogram, ref=np.max)

    with open(INDEX_PATH+'/'+file_name+'.npy', 'wb') as f:
        np.save(f, power_to_db)
    
    tmp_obj = {
        "length": audio_length,
        "tempo": tempo, 
        "beat_frames": beat_frames
    }
    with open(META_PATH+'/'+file_name+'.pkl', 'wb') as f:     
        pickle.dump(tmp_obj, f)
    
def generate_diagrams(input_file_dir):
    mp3_list = glob.glob(input_file_dir+"/*.mp3")
    for mp3_file_path in mp3_list:
        mp3_file_name = mp3_file_path.split("/")[-1].split(".")[0]
        with open("/".join(mp3_file_path.split("/")[:-1])+"/"+mp3_file_name+".pkl", 'rb')as f:
            mp3_length = pickle.load(f)
        generate_mel_diagram(mp3_file_path, mp3_length, mp3_file_name)

# def generate_diagrams(input_file_dir):
#     mp3_list = glob.glob(input_file_dir+"/*.mp3")
#     clip_audio(mp3_list, input_file_dir)