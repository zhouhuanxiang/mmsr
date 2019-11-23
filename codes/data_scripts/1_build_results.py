import os
import glob
import socket
import argparse


test_video_ids = [
    # '15398963809',
    # '15407349694',
    # '15439392361',
    # '15488420682',
    # '15523784704',
    # '16121597861',
    # '16064993671',
    # '15994056528',
    #     #
    # '15406724531',
    # '15627873950',
    # '15690684867',
    # '15752323646',
    # '15991733137',
    # '15898181711',
    # '15836862878'

    # '15415364550'
]

def parse_args():
    parser = argparse.ArgumentParser(description='extract raw frames')
    parser.add_argument('--models', nargs='+', 
                        help='tested models')
    parser.add_argument('--crfs', nargs='+', 
                        help='crfs of tested datasets')
    args = parser.parse_args()
    return args

'''
python ~/zhouhuanxiang/mmsr/codes/data_scripts/1_build_results.py \
--models MSRGANx1_KWAI40 MSRGANx1_KWAI40_1 MSRGANx1_KWAI40_2 MSRGANx1_KWAI40_3 MSRGANx1_KWAI40_4 \
--crfs 40 40 40 40 40

python ~/zhouhuanxiang/mmsr/codes/data_scripts/1_build_results.py \
--models EDVR_KWAI_2 \
--crfs 40

python ~/zhouhuanxiang/mmsr/codes/data_scripts/1_build_results.py \
--models TEMP \
--crfs 40

python ~/zhouhuanxiang/mmsr/codes/data_scripts/1_build_results.py \
--models test_SRResNet_ms_ssim_KWAI2530 test_SRResNet_ms_ssim_KWAI253035 test_SRResNet_ms_ssim_KWAI253035_slim7 test_SRResNet_ms_ssim_KWAI2530_slim7 \
--crfs 40 40 40 40

python ~/zhouhuanxiang/mmsr/codes/data_scripts/1_build_results.py \
--models test_SRResNet_ssim_KWAI2530 test_SRResNet_ssim_KWAI253035 test_SRResNet_ssim_KWAI253035_slim7 test_SRResNet_ssim_KWAI2530_slim7 \
--crfs 40 40 40 40

python ~/zhouhuanxiang/mmsr/codes/data_scripts/1_build_results.py \
--models test_SRResNet_ssim_KWAI40 test_SRResNet_ms_ssim_KWAI40 \
--crfs 40 40

python ~/zhouhuanxiang/mmsr/codes/data_scripts/1_build_results.py \
--models test_SRResNet_KWAI40_basline \
--crfs 40
'''

if __name__ == '__main__':
    # find ffmpeg
    if socket.gethostname() == 'sd-bjpg-hg27.yz02':
        ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg'
    elif socket.gethostname() == 'bjfk-hg29.yz02':
        ffmpeg = '/home/web_server/zhouhuanxiang/disk/ffmpeg_qlh/bin/ffmpeg'
    else:
        print('invalid new server!')

    args = parse_args()
    models = args.models
    crfs = args.crfs
    for crf, model in zip(crfs, models):
        # read images in img_path
        # write generated videos in video_path
        # read GT from original_path
        # if compare_path exists, concat videos in compare_path and video_path one by one,
        # if compare_path empty, compare with input
        img_path = '/home/web_server/zhouhuanxiang/disk/log/results/{}/KWAI-test'.format(model)
        video_path = '/home/web_server/zhouhuanxiang/disk/log/results/{}/KWAI-test-video'.format(model)
        concat_video_path = '/home/web_server/zhouhuanxiang/disk/log/results/{}/KWAI-test-video-concat'.format(model)
        # compare_path = '/home/web_server/zhouhuanxiang/disk/data/HD_UGC'
        # compare_path = '/home/web_server/zhouhuanxiang/disk/data/HD_UGC_crf{}'.format(crf)
        compare_path = '/home/web_server/zhouhuanxiang/disk/log/results/test_SRResNet_KWAI{}_basline/KWAI-test-video'.format(crf, crf)
        # compare_path = ''
        original_path = '/home/web_server/zhouhuanxiang/disk/data/HD_UGC'

        for path in [video_path, concat_video_path]:
            if os.path.exists(path):
                os.system('rm -rf {}'.format(path))
            os.makedirs(path, exist_ok=True)

        vids = glob.glob(os.path.join(img_path, '*'))
        vids = [vid.split('/')[-1] for vid in vids] 
        print(vids)

        for vid in vids:
            fps = os.popen("{} -i {} 2>&1 | sed -n \"s/.*, \(.*\) fp.*/\\1/p\"".format(ffmpeg, os.path.join(original_path, vid+'.mp4'))).read()
            fps = str(round(float(fps)))
            print('fps {}'.format(fps))

            ipath = os.path.join(img_path, vid)
            vpath = os.path.join(video_path, vid+'.mp4')
            os.system('{} -r {} -i {}/img_%5d.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y {}'
                            .format(ffmpeg, fps, ipath, vpath))
            if compare_path:
                cpath = os.path.join(compare_path, vid+'.mp4')
                cvpath = os.path.join(concat_video_path, vid+'.mp4')
                os.system('{} -i {} -i {} -filter_complex "[0:v:0]pad=iw*2:ih[bg]; [bg][1:v:0]overlay=w" -qp 10 {}'
                            .format(ffmpeg, cpath, vpath, cvpath))



'''
ffmpeg -i .mp4 2>&1 | sed -n "s/.*, \(.*\) fp.*/\1/p"
/usr/local/share/ffmpeg_qlh/bin/ffmpeg -r 30 -i 15398963809/img_%5d.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y 15398963809.mp4


os.system(ffmpeg+'-r '+str(fps)+' -i '+path+'/img_%5d.png -movflags +faststart -max_interleave_delta 150000000 -max_muxing_queue_size 9999 -c:v libx265 -psnr -threads 6 -preset fast -c:a copy -profile:a aac_he -ac 2 -x265-params lossless=1  -tag:v hvc1  -pix_fmt yuv420p -y '+path1)
os.system(ffmpeg+'-i '+path0+' -i '+path1+' -filter_complex "[0:v:0]pad=iw*2:ih[bg]; [bg][1:v:0]overlay=w" -qp 10 '+path2)

'''