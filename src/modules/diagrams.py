import os
import glob
from pydub import AudioSegment

AUDIO_CLIP_LENGTH = 2

def clip_audio(audio_list, output_path):
    for audio in audio_list:
        audio_seg = AudioSegment.from_file(audio)
        audio_filename = os.path.basename(audio).split(".")[0]
        audio_len = len(audio_seg)
        clipped = audio_seg[(audio_len - AUDIO_CLIP_LENGTH)/2: (audio_len + AUDIO_CLIP_LENGTH)/2]
        clipped.export(output_path + "/" + audio_filename + "_clipped.mp3", format="mp3")


def generate_mel_diagram():
    print()

def generate_diagrams(input_file_dir):
    mp3_list = glob.glob(input_file_dir+"/*.mp3")
    clip_audio(mp3_list, input_file_dir)