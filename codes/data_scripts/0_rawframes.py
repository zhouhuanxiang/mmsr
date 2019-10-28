import pickle
import glob
import os
import sys
import argparse
import socket
import cv2

def dump_frames(full_path, vname, out_full_path, is_train=True):
    if os.path.exists(out_full_path):
        os.system('rm -rf '+out_full_path)
    os.makedirs(out_full_path)
    # Read frame by ffmpeg
    os.system(ffmpeg+'-i '+full_path+' '+out_full_path+'/img_%05d.png -hide_banner')
    # clean
    if is_train:
        imgs_path = glob.glob(os.path.join(out_full_path, '*.png'))
        imgs_path.sort()
        
        print('total_frames', len(imgs_path))
        img_array = cv2.imread(imgs_path[0])
        if len(imgs_path) < 150 or img_array.shape != (1280, 720, 3):
            imgs_path_1 = []
        else:
            border = (len(imgs_path) - 100) // 2
            imgs_path_1 = imgs_path[border:border+100]
        imgs_path_2 = list(set(imgs_path) - set(imgs_path_1))
        for img in imgs_path_2:
            os.system('rm {}'.format(img))
        for i, img1 in enumerate(imgs_path_1):
            # os.system('mv {} img_{:0>5d}.png'.format(img, i))
            i0 = 'img_{:0>5d}.png'.format(i)
            i1 = 'img_{:0>5d}.png'.format(i + border + 1)
            img0 = img1.replace(i1, i0)
            os.system('mv {} {}'.format(img1, img0))

    print('video {} extracted'.format(vname))
    sys.stdout.flush()
    return True


def parse_args():
    parser = argparse.ArgumentParser(description='extract raw frames')
    parser.add_argument('--num_worker', type=int, default=8)
    parser.add_argument('--path', nargs='+',
                        help='path(s) of video folder to be extracted')
    parser.add_argument("--ext", type=str, default='mp4', choices=['avi', 'mp4', 'webm', 'flv'],
                        help='video file extensions')
    args = parser.parse_args()
    return args


'''

python 0_rawframes.py --path HD_UGC HD_UGC_crf35

'''

if __name__ == '__main__':
    args = parse_args()
    if socket.gethostname() == 'user-ubuntu':
        mode = 'lab'
    elif socket.gethostname() == 'ubuntu':
        mode = 'lab'
    elif socket.gethostname() == 'sd-bjpg-hg27.yz02':
        mode = 'kwai27'
    elif socket.gethostname() == 'bjfk-hg29.yz02':
        mode = 'kwai29'
    else:
        print('new server!')

    if mode == 'kwai27':
        prefix = '/home/web_server/zhouhuanxiang/disk'
        ffmpeg = '/usr/local/share/ffmpeg_qlh/bin/ffmpeg '
    elif mode == 'kwai29':
        prefix = '/home/web_server/zhouhuanxiang/disk'
        ffmpeg = 'ffmpeg '
    else:
        prefix = '/home1/zhx/disk'
        ffmpeg = 'ffmpeg '

    with open (os.path.join(prefix, 'vdata', 'HD_UGC_list'), 'rb') as fp:
        HD_UGC_train_list = pickle.load(fp)
    with open (os.path.join(prefix, 'vdata', 'HD_UGC_test_list'), 'rb') as fp:
        HD_UGC_test_list = pickle.load(fp)
    with open (os.path.join(prefix, 'vdata', 'HD_UGC_deleted_list'), 'rb') as fp:
        HD_UGC_deleted_list = pickle.load(fp)

    for path in args.path:
        for vname in HD_UGC_train_list:
            full_path = os.path.join(prefix, 'vdata', path, vname)
            out_full_path = os.path.join(prefix, 'vdata', path+'_raw', vname.split('.')[0])
            dump_frames(full_path, vname, out_full_path, True)

        for vname in HD_UGC_test_list:
            full_path = os.path.join(prefix, 'vdata', path, vname)
            out_full_path = os.path.join(prefix, 'vdata', path+'_raw_test', vname.split('.')[0])
            dump_frames(full_path, vname, out_full_path, False)