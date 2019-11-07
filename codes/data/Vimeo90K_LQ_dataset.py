import os.path as osp
import random
import torch
import numpy as np
import torch.utils.data as data
import data.util as util
import cv2


class VimeoLQDataset(data.Dataset):
    """
    A video test dataset. Support:
    Vid4 (x)
    REDS4 (x)
    Vimeo90K-Test

    no need to prepare LMDB files
    """

    def __init__(self, opt):
        super(VimeoLQDataset, self).__init__()
        self.opt = opt
        self.interval_list = opt['interval_list']
        self.random_reverse = opt['random_reverse']
        self.data_type = self.opt['data_type']
        self.half_N_frames = opt['N_frames'] // 2
        self.LQ_root0, self.LQ_root1, self.LQ_root2 = opt['dataroot_LQ0'], opt['dataroot_LQ1'], opt['dataroot_LQ2']
        self.LR_input = False if opt['GT_size'] == opt['LQ_size'] else True  # low resolution inputs

        #### determine the LQ frame list
        '''
        N | frames
        1 | 4
        3 | 3,4,5
        5 | 2,3,4,5,6
        7 | 1,2,3,4,5,6,7
        '''
        LQ_frames_list = []
        for i in range(opt['N_frames']):
            LQ_frames_list.append(i + (9 - opt['N_frames']) // 2)
        self.LQ_frames_set = set(LQ_frames_list)

        #### Generate data info and cache data
        if opt['name'].lower() in ['vimeo90k-lq']:
            subfolders_LQ0 = util.glob_file_in_file_list(self.LQ_root0)
            subfolders_LQ1 = util.glob_file_in_file_list(self.LQ_root1)
            subfolders_LQ2 = util.glob_file_in_file_list(self.LQ_root2)
            self.paths_LQ0 = subfolders_LQ0
            self.paths_LQ1 = subfolders_LQ1
            self.paths_LQ2 = subfolders_LQ2
            assert len(self.paths_LQ1) == len(self.paths_LQ0), 'LQ1 and LQ0 set should have same length'
            assert len(self.paths_LQ1) == len(self.paths_LQ2), 'LQ1 and LQ2 set should have same length'
        else:
            raise ValueError(
                'Not support video test dataset. Support Vimeo90k-Test.')

    def __getitem__(self, index):
        scale = self.opt['scale']
        LQ_size = self.opt['LQ_size']
        patch_size = self.opt['patch_size']
        patch_repeat = self.opt['patch_repeat']

        path_LQ0 = self.paths_LQ0[index]
        path_LQ1 = self.paths_LQ1[index]
        path_LQ2 = self.paths_LQ2[index]
        name_a, name_b = path_LQ0.split('/')[-2], path_LQ0.split('/')[-1]
        #### get LQ images
        LQ_size_tuple = (3, 64, 112) if self.LR_input else (3, 256, 448)
        img_LQ_l0 = []
        img_LQ_l1 = []
        img_LQ_l2 = []
        indices = random.sample(self.LQ_frames_set, 2)
        for v in indices:
            img_LQ0 = util.read_img(None,
                                   osp.join(self.LQ_root0, name_a, name_b, 'im{}.png'.format(v)))
            img_LQ_l0.append(img_LQ0)
            img_LQ1 = util.read_img(None,
                                   osp.join(self.LQ_root1, name_a, name_b, 'im{}.png'.format(v)))
            img_LQ_l1.append(img_LQ1)
            img_LQ2 = util.read_img(None,
                                   osp.join(self.LQ_root2, name_a, name_b, 'im{}.png'.format(v)))
            img_LQ_l2.append(img_LQ2)

        if self.opt['phase'] == 'train':
            C, H, W = LQ_size_tuple  # LQ size
            # randomly crop
            rnd_h = random.randint(0, max(0, H - LQ_size))
            rnd_w = random.randint(0, max(0, W - LQ_size))
            img_LQ_l0 = [v[rnd_h:rnd_h + LQ_size, rnd_w:rnd_w + LQ_size, :] for v in img_LQ_l0]
            img_LQ_l1 = [v[rnd_h:rnd_h + LQ_size, rnd_w:rnd_w + LQ_size, :] for v in img_LQ_l1]
            img_LQ_l2 = [v[rnd_h:rnd_h + LQ_size, rnd_w:rnd_w + LQ_size, :] for v in img_LQ_l2]

            # augmentation - flip, rotate
            img_LQ_l0.extend(img_LQ_l1)
            img_LQ_l0.extend(img_LQ_l2)
            rlt = util.augment(img_LQ_l0, self.opt['use_flip'], self.opt['use_rot'])
            img_LQ_l0 = rlt[0:2]
            img_LQ_l1 = rlt[2:4]
            img_LQ_l2 = rlt[4:]

        # TODO
        # img_LQ_l1[0] = img_LQ_l1[1].copy()

        patch_labels = []
        patch_offsets = []
        for j in range(patch_repeat):
            rnd_h = random.randint(0, max(0, LQ_size - patch_size))
            rnd_w = random.randint(0, max(0, LQ_size - patch_size))
            rnd_neighbor = random.sample(set([0, 2]), 1)[0]
            # TODO
            # rnd_neighbor = 2
            if rnd_neighbor == 0:
                img_LQ_l1[1][rnd_h:rnd_h + patch_size, rnd_w:rnd_w + patch_size, :] \
                    = img_LQ_l0[1][rnd_h:rnd_h + patch_size, rnd_w:rnd_w + patch_size, :]
                patch_labels.append(1.0)
            if rnd_neighbor == 2:
                img_LQ_l1[1][rnd_h:rnd_h + patch_size, rnd_w:rnd_w + patch_size, :] \
                    = img_LQ_l2[1][rnd_h:rnd_h + patch_size, rnd_w:rnd_w + patch_size, :]
                patch_labels.append(0.0)
            patch_offsets.append([[rnd_h, rnd_w]])

            # TODO
            # img_LQ_l1[1] = cv2.rectangle(img_LQ_l1[1], (rnd_w, rnd_h), (rnd_w + patch_size, rnd_h + patch_size), (0, 0, 255), 1)
            # if type(img_LQ_l1[1]) == cv2.UMat:
            #     img_LQ_l1[1] = img_LQ_l1[1].get()


        # TODO
        # stack LQ images to NHWC, N is the frame number
        img_LQ1s = np.stack(img_LQ_l1, axis=0)
        # BGR to RGB, HWC to CHW, numpy to tensor
        img_LQ1s = img_LQ1s[:, :, :, [2, 1, 0]]
        img_LQ1s = torch.from_numpy(np.ascontiguousarray(np.transpose(img_LQ1s,
                                                                     (0, 3, 1, 2)))).float()
        return {'LQs': img_LQ1s, 'key': name_a+'_'+name_b,
                'patch_labels': patch_labels,
                'patch_offsets': patch_offsets}

        # TODO
        # # stack LQ images to NHWC, N is the frame number
        # img_LQ0s = np.stack(img_LQ_l0, axis=0)
        # img_LQ1s = np.stack(img_LQ_l1, axis=0)
        # img_LQ2s = np.stack(img_LQ_l2, axis=0)
        # # BGR to RGB, HWC to CHW, numpy to tensor
        # img_LQ0s = img_LQ0s[:, :, :, [2, 1, 0]]
        # img_LQ1s = img_LQ1s[:, :, :, [2, 1, 0]]
        # img_LQ2s = img_LQ2s[:, :, :, [2, 1, 0]]
        # img_LQ0s = torch.from_numpy(np.ascontiguousarray(np.transpose(img_LQ0s,
        #                                                              (0, 3, 1, 2)))).float()
        # img_LQ1s = torch.from_numpy(np.ascontiguousarray(np.transpose(img_LQ1s,
        #                                                              (0, 3, 1, 2)))).float()
        # img_LQ2s = torch.from_numpy(np.ascontiguousarray(np.transpose(img_LQ2s,
        #                                                              (0, 3, 1, 2)))).float()
        # return {'LQ0s': img_LQ0s, 'LQ1s': img_LQ1s,
        #         'LQ2s': img_LQ2s, 'key': name_a+'_'+name_b,
        #         'patch_labels': patch_labels,
        #         'patch_offsets': patch_offsets}

    def __len__(self):
        return len(self.paths_LQ0)
