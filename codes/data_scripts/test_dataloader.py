import sys
import os.path as osp
import math
import torchvision.utils

sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from data import create_dataloader, create_dataset  # noqa: E402
from utils import util  # noqa: E402


def main():
    dataset = 'Vimeo90K_LQ'  # REDS | Vimeo90K | DIV2K800_sub
    opt = {}
    opt['dist'] = False
    opt['gpu_ids'] = [0]
    if dataset == 'LQGT':
        opt['name'] = 'test_KWAI'
        opt['dataroot_GT'] = '/home/web_server/zhouhuanxiang/disk/data/HD_UGC_raw'
        opt['dataroot_LQ'] = '/home/web_server/zhouhuanxiang/disk/data/HD_UGC_crf40_raw'
        opt['mode'] = 'LQGT'
        opt['color'] = 'RGB'
        opt['phase'] = 'train'
        opt['use_shuffle'] = True
        opt['n_workers'] = 1
        opt['batch_size'] = 4
        opt['GT_size'] = 256
        opt['LQ_size'] = 256
        opt['scale'] = 1
        opt['use_flip'] = True
        opt['use_rot'] = True
        opt['interval_list'] = [1]
        opt['random_reverse'] = False
        opt['border_mode'] = False
        opt['cache_keys'] = None
        opt['data_type'] = 'img'  # img | lmdb | mc
    elif dataset == 'KWAI':
        opt['name'] = 'test_KWAI'
        opt['dataroot_GT'] = '/home/web_server/zhouhuanxiang/disk/vdata/HD_UGC.lmdb'
        opt['dataroot_LQ'] = '/home/web_server/zhouhuanxiang/disk/vdata/HD_UGC_crf40.lmdb'
        opt['mode'] = 'KWAI'
        opt['N_frames'] = 5
        opt['phase'] = 'train'
        opt['use_shuffle'] = True
        opt['n_workers'] = 1
        opt['batch_size'] = 4
        opt['GT_size'] = 256
        opt['LQ_size'] = 256
        opt['scale'] = 1
        opt['use_flip'] = True
        opt['use_rot'] = True
        opt['interval_list'] = [1]
        opt['random_reverse'] = False
        opt['border_mode'] = False
        opt['cache_keys'] = None
        opt['data_type'] = 'lmdb'  # img | lmdb | mc
    elif dataset == 'REDS':
        opt['name'] = 'test_REDS'
        opt['dataroot_GT'] = '../../datasets/REDS/train_sharp_wval.lmdb'
        opt['dataroot_LQ'] = '../../datasets/REDS/train_sharp_bicubic_wval.lmdb'
        opt['mode'] = 'REDS'
        opt['N_frames'] = 5
        opt['phase'] = 'train'
        opt['use_shuffle'] = True
        opt['n_workers'] = 8
        opt['batch_size'] = 16
        opt['GT_size'] = 256
        opt['LQ_size'] = 64
        opt['scale'] = 4
        opt['use_flip'] = True
        opt['use_rot'] = True
        opt['interval_list'] = [1]
        opt['random_reverse'] = False
        opt['border_mode'] = False
        opt['cache_keys'] = None
        opt['data_type'] = 'lmdb'  # img | lmdb | mc
    elif dataset == 'Vimeo90K':
        opt['name'] = 'test_Vimeo90K'
        opt['dataroot_GT'] = '../../datasets/vimeo90k/vimeo90k_train_GT.lmdb'
        opt['dataroot_LQ'] = '../../datasets/vimeo90k/vimeo90k_train_LR7frames.lmdb'
        opt['mode'] = 'Vimeo90K'
        opt['N_frames'] = 7
        opt['phase'] = 'train'
        opt['use_shuffle'] = True
        opt['n_workers'] = 8
        opt['batch_size'] = 16
        opt['GT_size'] = 256
        opt['LQ_size'] = 64
        opt['scale'] = 4
        opt['use_flip'] = True
        opt['use_rot'] = True
        opt['interval_list'] = [1]
        opt['random_reverse'] = False
        opt['border_mode'] = False
        opt['cache_keys'] = None
        opt['data_type'] = 'lmdb'  # img | lmdb | mc
    elif dataset == 'Vimeo90K_test':
        opt['name'] = 'vimeo90k-test'
        opt['dataroot_GT'] = '/home/web_server/zhouhuanxiang/disk/vimeo/vimeo_septuplet/sequences'
        opt['dataroot_LQ'] = '/home/web_server/zhouhuanxiang/disk/vimeo/vimeo_septuplet/sequences_blocky32'
        opt['mode'] = 'Vimeo90K_test'
        opt['all_gt'] = True
        opt['N_frames'] = 7
        opt['phase'] = 'train'
        opt['use_shuffle'] = True
        opt['n_workers'] = 8
        opt['batch_size'] = 16
        opt['GT_size'] = 256
        opt['LQ_size'] = 256
        opt['scale'] = 1
        opt['use_flip'] = True
        opt['use_rot'] = True
        opt['interval_list'] = [1]
        opt['random_reverse'] = False
        opt['border_mode'] = False
        opt['cache_keys'] = None
        opt['data_type'] = 'img'  # img | lmdb | mc
    elif dataset == 'Vimeo90K_LQ':
        opt['name'] = 'Vimeo90K-LQ'
        opt['dataroot_LQ0'] = '/home/web_server/zhouhuanxiang/disk/vimeo/vimeo_septuplet/sequences_blocky32'
        opt['dataroot_LQ1'] = '/home/web_server/zhouhuanxiang/disk/vimeo/vimeo_septuplet/sequences_blocky37'
        opt['dataroot_LQ2'] = '/home/web_server/zhouhuanxiang/disk/vimeo/vimeo_septuplet/sequences_blocky42'
        opt['mode'] = 'Vimeo90K_LQ'
        opt['patch_size'] = 32
        opt['patch_repeat'] = 5
        opt['N_frames'] = 7
        opt['phase'] = 'train'
        opt['use_shuffle'] = True
        opt['n_workers'] = 8
        opt['batch_size'] = 16
        opt['GT_size'] = 256
        opt['LQ_size'] = 256
        opt['scale'] = 1
        opt['use_flip'] = True
        opt['use_rot'] = True
        opt['interval_list'] = [1]
        opt['random_reverse'] = False
        opt['border_mode'] = False
        opt['cache_keys'] = None
        opt['data_type'] = 'img'  # img | lmdb | mc
    elif dataset == 'DIV2K800_sub':
        opt['name'] = 'DIV2K800'
        opt['dataroot_GT'] = '../../datasets/DIV2K/DIV2K800_sub.lmdb'
        opt['dataroot_LQ'] = '../../datasets/DIV2K/DIV2K800_sub_bicLRx4.lmdb'
        opt['mode'] = 'LQGT'
        opt['phase'] = 'train'
        opt['use_shuffle'] = True
        opt['n_workers'] = 8
        opt['batch_size'] = 16
        opt['GT_size'] = 128
        opt['scale'] = 4
        opt['use_flip'] = True
        opt['use_rot'] = True
        opt['color'] = 'RGB'
        opt['data_type'] = 'lmdb'  # img | lmdb
    else:
        raise ValueError('Please implement by yourself.')

    util.mkdir('/home/web_server/zhouhuanxiang/tmp')
    train_set = create_dataset(opt)
    train_loader = create_dataloader(train_set, opt, opt, None)
    nrow = int(math.sqrt(opt['batch_size']))
    padding = 2 if opt['phase'] == 'train' else 0

    print('start...')
    for i, data in enumerate(train_loader):
        if i > 5:
            break
        print(i)


        LQ0s = data['LQ0s']
        LQ1s = data['LQ1s']
        LQ2s = data['LQ2s']
        patch_offsets = data['patch_offsets']
        print(patch_offsets)

        for j in range(LQ0s.size(1)):
            torchvision.utils.save_image(LQ0s[:, j, :, :, :],
                                         '/home/web_server/zhouhuanxiang/tmp/LQ0_{:03d}_{}.png'.format(i, j), nrow=nrow,
                                         padding=padding, normalize=False)
        for j in range(LQ1s.size(1)):
            torchvision.utils.save_image(LQ1s[:, j, :, :, :],
                                         '/home/web_server/zhouhuanxiang/tmp/LQ1_{:03d}_{}.png'.format(i, j), nrow=nrow,
                                         padding=padding, normalize=False)
        for j in range(LQ2s.size(1)):
            torchvision.utils.save_image(LQ2s[:, j, :, :, :],
                                         '/home/web_server/zhouhuanxiang/tmp/LQ2_{:03d}_{}.png'.format(i, j), nrow=nrow,
                                         padding=padding, normalize=False)

    # for i, data in enumerate(train_loader):
    #     if i > 5:
    #         break
    #     print(i)
    #     if dataset == 'REDS' or dataset == 'Vimeo90K' or dataset == 'KWAI' or dataset == 'Vimeo90K_test':
    #         LQs = data['LQs']
    #     else:
    #         LQ = data['LQ']
    #     if dataset == 'Vimeo90K_test' and opt['all_gt']:
    #         GTs = data['GTs']
    #     else:
    #         GT = data['GT']
    #
    #     if dataset == 'REDS' or dataset == 'Vimeo90K' or dataset == 'KWAI' or dataset == 'Vimeo90K_test':
    #         for j in range(LQs.size(1)):
    #             torchvision.utils.save_image(LQs[:, j, :, :, :],
    #                                          '/home/web_server/zhouhuanxiang/tmp/LQ_{:03d}_{}.png'.format(i, j), nrow=nrow,
    #                                          padding=padding, normalize=False)
    #     else:
    #         torchvision.utils.save_image(LQ, '/home/web_server/zhouhuanxiang/tmp/LQ_{:03d}.png'.format(i), nrow=nrow,
    #                                      padding=padding, normalize=False)
    #
    #     if dataset == 'Vimeo90K_test' and opt['all_gt']:
    #         for j in range(GTs.size(1)):
    #             torchvision.utils.save_image(GTs[:, j, :, :, :],
    #                                          '/home/web_server/zhouhuanxiang/tmp/GT_{:03d}_{}.png'.format(i, j),
    #                                          nrow=nrow,
    #                                          padding=padding, normalize=False)
    #     else:
    #         torchvision.utils.save_image(GT, '/home/web_server/zhouhuanxiang/tmp/GT_{:03d}.png'.format(i), nrow=nrow, padding=padding,
    #                                      normalize=False)


if __name__ == "__main__":
    main()


# python ~/zhouhuanxiang/mmsr/codes/data_scripts/test_dataloader.py