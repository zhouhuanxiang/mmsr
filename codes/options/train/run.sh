#!/usr/bin/env bash
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI35.yml > ~/zhouhuanxiang/gan35 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40.yml > ~/zhouhuanxiang/gan40 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI45.yml > ~/zhouhuanxiang/gan45 2>&1 &

nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40_1.yml > ~/zhouhuanxiang/gan40_1 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40_2.yml > ~/zhouhuanxiang/gan40_2 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40_3.yml > ~/zhouhuanxiang/gan40_3 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40_4.yml > ~/zhouhuanxiang/gan40_4 2>&1 &

nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRGAN_KWAI40.yml > ~/zhouhuanxiang/t_gan40 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRGAN_KWAI40_1.yml > ~/zhouhuanxiang/t_gan40_1 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRGAN_KWAI40_2.yml > ~/zhouhuanxiang/t_gan40_2 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRGAN_KWAI40_3.yml > ~/zhouhuanxiang/t_gan40_3 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRGAN_KWAI40_4.yml > ~/zhouhuanxiang/t_gan40_4 2>&1 &

nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40.yml > ~/zhouhuanxiang/srresnet40 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRGAN_KWAI40_origin.yml > ~/zhouhuanxiang/t_srgan40_origin 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRGAN_KWAI40_EDSR.yml > ~/zhouhuanxiang/t_srgan40_EDSR 2>&1 &

nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40_origin_1.yml > ~/zhouhuanxiang/gan40_1 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40_origin_2.yml > ~/zhouhuanxiang/gan40_2 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40_origin_3.yml > ~/zhouhuanxiang/gan40_3 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40_origin_4.yml > ~/zhouhuanxiang/gan40_4 2>&1 &

nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40_pretrain_3.yml > ~/zhouhuanxiang/pre3 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRGAN_KWAI40_pretrain_4.yml > ~/zhouhuanxiang/pre4 2>&1 &

nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_CX_1.yml > ~/zhouhuanxiang/cx1 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_CX_2.yml > ~/zhouhuanxiang/cx2 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_CX_3.yml > ~/zhouhuanxiang/cx3 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_CX_4.yml > ~/zhouhuanxiang/cx4 2>&1 &

nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_slim0.yml > ~/zhouhuanxiang/slim0 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_slim1.yml > ~/zhouhuanxiang/slim1 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_slim2.yml > ~/zhouhuanxiang/slim2 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_slim3.yml > ~/zhouhuanxiang/slim3 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_slim4.yml > ~/zhouhuanxiang/slim4 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_slim5.yml > ~/zhouhuanxiang/slim5 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_slim6.yml > ~/zhouhuanxiang/slim6 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_slim7.yml > ~/zhouhuanxiang/slim7 2>&1 &

nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRResNet_KWAI40_slim0.yml > ~/zhouhuanxiang/t_slim0 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRResNet_KWAI40_slim1.yml > ~/zhouhuanxiang/t_slim1 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRResNet_KWAI40_slim2.yml > ~/zhouhuanxiang/t_slim2 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRResNet_KWAI40_slim3.yml > ~/zhouhuanxiang/t_slim3 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRResNet_KWAI40_slim4.yml > ~/zhouhuanxiang/t_slim4 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRResNet_KWAI40_slim5.yml > ~/zhouhuanxiang/t_slim5 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRResNet_KWAI40_slim6.yml > ~/zhouhuanxiang/t_slim6 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/test_SRResNet_KWAI40_slim7.yml > ~/zhouhuanxiang/t_slim7 2>&1 &


nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_EDVR_KWAI40_woTSA_M.yml > ~/zhouhuanxiang/EDVR_woTSA_M 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_EDVR_KWAI40_M.yml > ~/zhouhuanxiang/EDVR_M 2>&1 &


nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_baseline25.yml > ~/zhouhuanxiang/baseline25 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_baseline30.yml > ~/zhouhuanxiang/baseline30 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_baseline35.yml > ~/zhouhuanxiang/baseline35 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_baseline40.yml > ~/zhouhuanxiang/baseline40 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI40_baseline45.yml > ~/zhouhuanxiang/baseline45 2>&1 &


nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI2530_slim8.yml > ~/zhouhuanxiang/train_SRResNet_KWAI2530_slim8 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI2530_slim9.yml > ~/zhouhuanxiang/train_SRResNet_KWAI2530_slim9 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI2530_slim10.yml > ~/zhouhuanxiang/train_SRResNet_KWAI2530_slim10 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI2530_slim11.yml > ~/zhouhuanxiang/train_SRResNet_KWAI2530_slim11 2>&1 &


nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI253035.yml > ~/zhouhuanxiang/train_SRResNet_KWAI253035 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_SRResNet_KWAI253035_slim7.yml > ~/zhouhuanxiang/train_SRResNet_KWAI253035_slim7 2>&1 &


nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_UNet_attention_u256_wDiff.yml >  ~/zhouhuanxiang/train_UNet_attention_u256_wDiff 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/train_UNet_attention_u256_woDiff.yml >  ~/zhouhuanxiang/train_UNet_attention_u256_woDiff 2>&1 &


# ssim train
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ssim_KWAI2530.yml > ~/zhouhuanxiang/train_SRResNet_ssim_KWAI2530 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ms_ssim_KWAI2530.yml > ~/zhouhuanxiang/train_SRResNet_ms_ssim_KWAI2530 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ssim_KWAI253035.yml > ~/zhouhuanxiang/train_SRResNet_ssim_KWAI253035 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ms_ssim_KWAI253035.yml > ~/zhouhuanxiang/train_SRResNet_ms_ssim_KWAI253035 2>&1 &

nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ssim_KWAI2530_slim7.yml > ~/zhouhuanxiang/train_SRResNet_ssim_KWAI2530_slim7 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ms_ssim_KWAI2530_slim7.yml > ~/zhouhuanxiang/train_SRResNet_ms_ssim_KWAI2530_slim7 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ssim_KWAI253035_slim7.yml > ~/zhouhuanxiang/train_SRResNet_ssim_KWAI253035_slim7 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ms_ssim_KWAI253035_slim7.yml > ~/zhouhuanxiang/train_SRResNet_ms_ssim_KWAI253035_slim7 2>&1 &
# ssim test
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/ssim/test_SRResNet_ssim_KWAI2530.yml > ~/zhouhuanxiang/test_SRResNet_ssim_KWAI2530 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/ssim/test_SRResNet_ms_ssim_KWAI2530.yml > ~/zhouhuanxiang/test_SRResNet_ms_ssim_KWAI2530 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/ssim/test_SRResNet_ssim_KWAI253035.yml > ~/zhouhuanxiang/test_SRResNet_ssim_KWAI253035 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/ssim/test_SRResNet_ms_ssim_KWAI253035.yml > ~/zhouhuanxiang/test_SRResNet_ms_ssim_KWAI253035 2>&1 &

nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/ssim/test_SRResNet_ssim_KWAI2530_slim7.yml > ~/zhouhuanxiang/test_SRResNet_ssim_KWAI2530_slim7 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/ssim/test_SRResNet_ms_ssim_KWAI2530_slim7.yml > ~/zhouhuanxiang/test_SRResNet_ms_ssim_KWAI2530_slim7 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/ssim/test_SRResNet_ssim_KWAI253035_slim7.yml > ~/zhouhuanxiang/test_SRResNet_ssim_KWAI253035_slim7 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/ssim/test_SRResNet_ms_ssim_KWAI253035_slim7.yml > ~/zhouhuanxiang/test_SRResNet_ms_ssim_KWAI253035_slim7 2>&1 &
# 11 & 21 & 31 train
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ssim_KWAI35_11.yml > ~/zhouhuanxiang/train_SRResNet_ssim_KWAI35_11 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ssim_KWAI35_21.yml > ~/zhouhuanxiang/train_SRResNet_ssim_KWAI35_21 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ssim_KWAI35_31.yml > ~/zhouhuanxiang/train_SRResNet_ssim_KWAI35_31 2>&1 &
# 11 & 21 & 31 test

# 40 train
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ssim_KWAI40.yml > ~/zhouhuanxiang/train_SRResNet_ssim_KWAI40 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/ssim/train_SRResNet_ms_ssim_KWAI40.yml > ~/zhouhuanxiang/train_SRResNet_ms_ssim_KWAI40 2>&1 &
# 40 test
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/ssim/test_SRResNet_ssim_KWAI40.yml > ~/zhouhuanxiang/test_SRResNet_ssim_KWAI40 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/ssim/test_SRResNet_ms_ssim_KWAI40.yml > ~/zhouhuanxiang/test_SRResNet_ms_ssim_KWAI40 2>&1 &

# retrain bsaeline
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/SRResNet/train_SRResNet_KWAI25_baseline.yml > ~/zhouhuanxiang/train_SRResNet_KWAI25_baseline 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/SRResNet/train_SRResNet_KWAI30_baseline.yml > ~/zhouhuanxiang/train_SRResNet_KWAI30_baseline 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/SRResNet/train_SRResNet_KWAI35_baseline.yml > ~/zhouhuanxiang/train_SRResNet_KWAI35_baseline 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/SRResNet/train_SRResNet_KWAI40_baseline.yml > ~/zhouhuanxiang/train_SRResNet_KWAI40_baseline 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/SRResNet/train_SRResNet_KWAI45_baseline.yml > ~/zhouhuanxiang/train_SRResNet_KWAI45_baseline 2>&1 &
# retest baseline
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/SRResNet/test_SRResNet_KWAI25_baseline.yml > ~/zhouhuanxiang/test_SRResNet_KWAI25_baseline 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/SRResNet/test_SRResNet_KWAI30_baseline.yml > ~/zhouhuanxiang/test_SRResNet_KWAI30_baseline 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/SRResNet/test_SRResNet_KWAI35_baseline.yml > ~/zhouhuanxiang/test_SRResNet_KWAI35_baseline 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/SRResNet/test_SRResNet_KWAI40_baseline.yml > ~/zhouhuanxiang/test_SRResNet_KWAI40_baseline 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/test.py -opt ~/zhouhuanxiang/mmsr/codes/options/test/SRResNet/test_SRResNet_KWAI45_baseline.yml > ~/zhouhuanxiang/test_SRResNet_KWAI45_baseline 2>&1 &

# vmaf train
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/vmaf/train_SRResNet_vmaf_KWAI35.yml > ~/zhouhuanxiang/train_SRResNet_vmaf_KWAI35 2>&1 &
nohup python ~/zhouhuanxiang/mmsr/codes/train.py -opt ~/zhouhuanxiang/mmsr/codes/options/train/vmaf/train_SRResNet_vmaf_KWAI40.yml > ~/zhouhuanxiang/train_SRResNet_vmaf_KWAI40 2>&1 &

