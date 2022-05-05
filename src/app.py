import sys
import os

from modules import scene_detect, clip_video, diagrams

# Set Directories
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
sys.path.append(ROOT_DIR)

INPUT_FILE = "/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/src/resources/sanda_moduwela.mp4"
FORMATTED_DIR = "/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/src/resources/formatted_files"
OUTPUT_FILE_NAME = "2"

# scenes = scene_detect.find_scenes(INPUT_FILE)
# clip_video.clip_video_from_list(INPUT_FILE, scenes, FORMATTED_DIR+"/"+OUTPUT_FILE_NAME)


# diagrams.generate_mel_diagram(FORMATTED_DIR+"/"+OUTPUT_FILE_NAME+"_1.mp3", FORMATTED_DIR+"/"+OUTPUT_FILE_NAME+"_1")
# diagrams.generate_diagrams(FORMATTED_DIR)

# Move Video Files
import shutil
import glob

IN_PATH = FORMATTED_DIR
OUT_PATH = "/home/sahan/Desktop/Projects/DataDisca/Music_Video_Generator/src/db/meta"
mp4_list = glob.glob(IN_PATH+"/*.mp4")

for mp4_file in mp4_list:
    shutil.move(mp4_file, OUT_PATH+"/"+mp4_file.split("/")[-1])

print("Done")