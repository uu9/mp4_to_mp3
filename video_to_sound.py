import os
import time
from moviepy.editor import *

start_time = time.time()
target_dir = "path_to_save"
path_to_walk = "path_to_convert"
all_files_name = []
for a, b, c in os.walk(target_dir):
    all_files_name += c
for root, dirs, files in os.walk(path_to_walk):
    for i in files:
        if i.replace(".mp4", ".mp3") not in all_files_name:
            print(os.path.join(target_dir, os.path.basename(root), os.path.splitext(i)[0]+".mp3"))
            #print(i.replace(".mp4", ".mp3"), all_files_name)
            full_name = os.path.join(root, i)
            video = VideoFileClip(full_name)
            audio = video.audio
            if not os.path.exists(os.path.join(target_dir, os.path.basename(root))):
                os.makedirs(os.path.join(target_dir, os.path.basename(root)))
            audio.write_audiofile(os.path.join(target_dir, os.path.basename(root), os.path.splitext(i)[0]+".mp3"))
end_time = time.time()
used_time = end_time-start_time
print(time.asctime(time.localtime(used_time)))
print(time.asctime(time.localtime(time.time())))
