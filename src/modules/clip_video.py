from moviepy.editor import *
import pickle


def clip_video(input_file, start_time, end_time, output_file):
    clip = VideoFileClip(input_file).subclip(start_time, end_time)

    # Get Clip Duration
    duration = clip.duration
    if duration < 2:
        return 0

    audio_clip = clip.subclip(duration/2 - 0.5, duration/2 + 0.5).audio
    video_clip = clip.without_audio()

    # Save Duration
    with open(output_file+".pkl", 'wb') as handle:
        pickle.dump(duration, handle)

    audio_clip.write_audiofile(output_file+".mp3")
    video_clip.write_videofile(output_file+".mp4")

def clip_video_from_list(input_file, scene_list, output_file):
    for idx, scene in enumerate(scene_list):
        clip_video(input_file, scene[0].get_seconds(), scene[1].get_seconds(), output_file+"_"+str(idx))