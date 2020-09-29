import os
import time
from moviepy.editor import *

start_time = time.time()
target_dir = "E:\迅雷下载\恋词真题5500（原绿皮书）\纯音频文件"
all_files_name = []
for a, b, c in os.walk("E:\迅雷下载\恋词真题5500（原绿皮书）\纯音频文件"):
    all_files_name += c
for root, dirs, files in os.walk("E:\迅雷下载\恋词真题5500（原绿皮书）\大黄《考研英语真题5500词》配套视频"):
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
# root, dirs, files = os.walk("E:\迅雷下载\恋词真题5500（原绿皮书）\大黄《考研英语真题5500词》配套视频\L1")
end_time = time.time()
used_time = end_time-start_time
print(time.asctime(time.localtime(used_time)))
print(time.asctime(time.localtime(time.time())))
