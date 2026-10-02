import os
import webvtt
from datetime import datetime

def convert_vtt_to_lrc(vtt_filename,lrc_filename):
    print(f"正在將{vtt_filename}\n轉換為{lrc_filename}")
    vtt=webvtt.read(vtt_filename)
    with open(lrc_filename,'w',encoding='utf-8') as f:
        for caption in vtt:
            start=datetime.strptime(caption.start,'%H:%M:%S.%f')
            f.write(f"[{start.minute}:{start.second:02}.{start.microsecond//10000}]{caption.text}\n")
while True:
    folder = input("輸入位址 Q離開:")
    if folder.lower() == 'q':
        break
    print(f"打開資料夾:{folder}")

    for filename in os.listdir(folder):
        if filename.endswith('.vtt'):
            base_filename = os.path.splitext(filename)[0]
            vtt_filename = os.path.join(folder,filename)
            lrcN = filename.replace('.vtt','.lrc')
            lrc_filename = os.path.join(folder,lrcN)
            convert_vtt_to_lrc(vtt_filename,lrc_filename)
    


