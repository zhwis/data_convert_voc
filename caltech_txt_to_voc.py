#! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image
import shutil
from scipy.io import loadmat
#img_Lists = glob.glob(src_img_dir + '\*.png')
 
# caltech图像的标注位置
src_anno_dir = 'test_name.txt'

# caltech图像的存储位置
src_img_dir = "/zhihui/ssd_caltech/caffe-ssd/data/caltech/test/images"

#保存为VOC 数据集的原图和xml标注路径
new_img= "/zhihui/ssd_caltech/caffe-ssd/data/caltech/test/JPEGImages"
new_xml= "/zhihui/ssd_caltech/caffe-ssd/data/caltech/test/Annotations"

if not os.path.isdir(new_img):
	os.makedirs(new_img)
    
if not os.path.isdir(new_xml):
	os.makedirs(new_xml)   

txt_dir = "/zhihui/ssd_caltech/caffe-ssd/data/caltech/"
anno_dir = 'test/annotations'
count = 0
with open(os.path.join(txt_dir, src_anno_dir),"r") as f1:     
	for line in f1:
		img_name = line.strip('\n')
		img_full_path=src_img_dir+"/"+img_name+'.jpg'

		shutil.copy(img_full_path, new_img+"/"+img_name+'.jpg')
		img=Image.open(img_full_path)
		width, height = img.size
		with open(os.path.join(txt_dir+anno_dir, img_name +'.txt'),"r") as f2:
			xml_file = open((new_xml + '/' + img_name + '.xml'), 'w')	  
			xml_file.write('<annotation>\n')
			xml_file.write('    <folder>caltech</folder>\n')
			xml_file.write('    <filename>' + str(img_name)+'.jpg'+ '</filename>\n')
			xml_file.write('    <size>\n')
			xml_file.write('        <width>' + str(640) + '</width>\n')
			xml_file.write('        <height>' + str(480) + '</height>\n')
			xml_file.write('        <depth>3</depth>\n')
			xml_file.write('    </size>\n')

			for txt_line in f2:	

				info = txt_line.strip('\n').split(' ')
				category, xmin, ymin, xmax, ymax = int(info[0]), info[1], info[2], info[3], info[4]
				#sub_category = int(category)
				if category == 1:
					#x=category_location[1]   #class_label==1 or 2: x1，y1，w，h；
					#y=category_location[2]
					#w=category_location[3]
					#h=category_location[4]


					xml_file.write('    <object>\n')
					xml_file.write('        <name>' + 'person' + '</name>\n')
					xml_file.write('        <pose>Unspecified</pose>\n')
					xml_file.write('        <truncated>0</truncated>\n')
					xml_file.write('        <difficult>0</difficult>\n')
					xml_file.write('        <bndbox>\n')
					xml_file.write('            <xmin>' + xmin + '</xmin>\n')
					xml_file.write('            <ymin>' + ymin + '</ymin>\n')
					xml_file.write('            <xmax>' + xmax + '</xmax>\n')
					xml_file.write('            <ymax>' + ymax + '</ymax>\n')
					xml_file.write('        </bndbox>\n')
					xml_file.write('    </object>\n')
				else:
					count += 1
					print("current image is:",img_full_path)
			xml_file.write('</annotation>\n')
