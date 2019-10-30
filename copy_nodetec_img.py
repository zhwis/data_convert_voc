#! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image
import shutil
from scipy.io import loadmat
#img_Lists = glob.glob(src_img_dir + '\*.png')
 
# caltech图像的标注位置
#src_anno_dir = 'test_name.txt'

# 原图像的存储位置
src_img_dir = "/zhihui/DMS/state-farm-distracted-driver-detection/imgs/train/c3"
txt_dir = "/zhihui/DMS/darknet/results/c3/labels"
empty_img = "/zhihui/DMS/darknet/results/c3/empty"

if not os.path.isdir(empty_img):
	os.makedirs(empty_img)

for txt_name in os.listdir(txt_dir):
	size = os.path.getsize(os.path.join(txt_dir, txt_name))
	if not size:
		img_name = txt_name.split('.')[0]
		img_full_path=src_img_dir+"/"+img_name+'.jpg'
		shutil.copy(img_full_path, empty_img+"/"+"1_"+img_name+'.jpg')

		#continue
	else:
		continue
		'''
		img_name = txt_name.split('.')[0]
		img_full_path=src_img_dir+"/"+img_name+'.jpg'
		shutil.copy(img_full_path, new_img+"/"+"1_"+img_name+'.jpg')
		'''

