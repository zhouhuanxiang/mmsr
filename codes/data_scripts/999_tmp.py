# '''
# baseline vs patch
# '''
# import os
# import socket
# import argparse

# video_names = [
#     '15398963809',
#     '15407349694',
#     '15439392361',
#     '15488420682',
#     '15523784704',
#     '16121597861',
#     '16064993671',
#     '15994056528',
#     #
#     '15406724531',
#     '15627873950',
#     '15690684867',
#     '15752323646',
#     '15991733137',
#     '15898181711',
#     '15836862878'
# ]

# ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg '
# folder = '/home/web_server/zhouhuanxiang/disk/compare'
# os.makedirs(folder, exist_ok=True)

# for crf in ['35', '40', '45']:
#     os.makedirs(os.path.join(folder, 'crf'+crf), exist_ok=True)
#     for vname in video_names:
#         path0 = '~/zhouhuanxiang/disk/log_prev/log_20190905/EDSR_crf'+crf+'_baseline/videos-KWAIVIDEO-crf'+crf+'_tmp/'+vname+'_tmp.mp4'
#         path1 = '~/zhouhuanxiang/disk/log/results/MSRGANx1_KWAI'+crf+'/KWAI-test-video_tmp/'+vname+'_tmp.mp4'
#         path2 = os.path.join(folder, 'crf'+crf, vname+'.mp4')
#         os.system(ffmpeg+'-i '+path0+' -i '+path1+' -filter_complex "[0:v:0]pad=iw*2:ih[bg]; [bg][1:v:0]overlay=w" -qp 10 '+path2)
# '''
# python ~/zhouhuanxiang/mmsr/codes/data_scripts/999_tmp.py
# '''

import glob
import cv2
import numpy as np

p1 = glob.glob('/home/web_server/zhouhuanxiang/disk/data/HD_UGC_raw/*/*.png')
p2 = glob.glob('/home/web_server/zhouhuanxiang/disk/data/HD_UGC_crf40_raw/*/*.png')

p1.sort()
p2.sort()

print(len(p1), len(p2))

for i1, i2 in list(zip(p1, p2)):
    img1 = cv2.imread(i1)
    img2 = cv2.imread(i2)
    mse = np.mean((img1 - img2)**2)
    print(mse)
