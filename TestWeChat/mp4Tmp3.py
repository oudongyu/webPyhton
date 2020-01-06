import os
import glob
from pydub import AudioSegment

dir = []
path = input("请输入要转码的父文件夹：")
for root, dirs, files in os.walk(path):
    dir.append(root)

for d in dir:
    os.chdir(d)
    extension_list = ('*.mp4', '*.flv')
    for extension in extension_list:
        for video in glob.glob(extension):
            # print(os.getcwd())
            # print(video)D:\视频\斗鱼
            splitext = os.path.splitext(os.path.basename(video))[0] + ".mp3"
            # print(splitext)
            print(os.path.join(d,video))
            AudioSegment.from_file(os.path.join(d,video)).export(splitext, format="mp3")
            print('已转码' + splitext)
