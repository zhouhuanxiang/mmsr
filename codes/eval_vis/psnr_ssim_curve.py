import numpy as np
from numpy import loadtxt

psnrAll = loadtxt('/Users/zhx/Desktop/1/psnrAll.txt', comments='#', delimiter='\n', unpack=False)
ssimAll = loadtxt('/Users/zhx/Desktop/1/ssimAll.txt', comments='#', delimiter='\n', unpack=False)
print(' mean PSNR ', np.mean(psnrAll), ' mean SSIM ', np.mean(ssimAll), '\n')

sep_testlist = loadtxt('/Users/zhx/Desktop/sep_testlist.txt', dtype=str)
psnrAll = list(zip(psnrAll, sep_testlist))
ssimAll = list(zip(ssimAll, sep_testlist))
print(psnrAll[:10])
print(ssimAll[:10], '\n')

psnrAll = sorted(psnrAll, key=lambda tup: tup[0])
ssimAll = sorted(ssimAll, key=lambda tup: tup[0])
print(psnrAll[:10])
print(ssimAll[:10], '\n')



