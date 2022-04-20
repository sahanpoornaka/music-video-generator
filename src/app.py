import sys
import os
import sys

from modules import scene_detect, clip_video, diagrams

# Set Directories
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
sys.path.append(ROOT_DIR)

INPUT_FILE = "/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/resources/music_video/mal_kakuli.mp4"
FORMATTED_DIR = "/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/resources/formatted_files"

# scenes = scene_detect.find_scenes(INPUT_FILE)
# clip_video.clip_video(INPUT_FILE, scenes, FORMATTED_DIR+"/"+str(1))

diagrams.generate_diagrams(FORMATTED_DIR)
