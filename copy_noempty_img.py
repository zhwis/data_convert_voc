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
src_img_dir = "/opt/project/YOLO-master/darknet/results/cell_phone/phone"

#保存为VOC 数据集的原图和xml标注路径
new_img= "/opt/project/YOLO-master/darknet/results/new_cell_phone/JPEGImages"
new_xml= "/opt/project/YOLO-master/darknet/results/new_cell_phone/Annotations"
empty_img = "/opt/project/YOLO-master/darknet/results/new_cell_phone/empty"

if not os.path.isdir(new_img):
	os.makedirs(new_img)
    
if not os.path.isdir(new_xml):
	os.makedirs(new_xml)   

txt_dir = "/opt/project/YOLO-master/darknet/results/new_cell_phone/labels_c2_r"
# anno_dir = 'test/annotations'
for txt_name in os.listdir(txt_dir):
	size = os.path.getsize(os.path.join(txt_dir, txt_name))
	if not size:
		img_name = txt_name.split('.')[0]
		img_full_path=src_img_dir+"/"+img_name+'.jpg'
		shutil.copy(img_full_path, empty_img+"/"+"1_"+img_name+'.jpg')

		#continue
	else:
		img_name = txt_name.split('.')[0]
		img_full_path=src_img_dir+"/"+img_name+'.jpg'
		shutil.copy(img_full_path, new_img+"/"+"1_"+img_name+'.jpg')

