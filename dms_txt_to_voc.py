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

# caltech图像的存储位置
src_img_dir = "/opt/project/YOLO-master/darknet/results/cell_phone/phone"

#保存为VOC 数据集的原图和xml标注路径
new_img= "/opt/project/YOLO-master/darknet/results/new_cell_phone/JPEGImages"
new_xml= "/opt/project/YOLO-master/darknet/results/new_cell_phone/Annotations"

if not os.path.isdir(new_img):
	os.makedirs(new_img)
    
if not os.path.isdir(new_xml):
	os.makedirs(new_xml)   

txt_dir = "/opt/project/YOLO-master/darknet/results/new_cell_phone/labels_c2_r"
# anno_dir = 'test/annotations'
count = 0

for txt_name in os.listdir(txt_dir):
	size = os.path.getsize(os.path.join(txt_dir, txt_name))
	if not size:
		continue
	else:
		with open(os.path.join(txt_dir, txt_name),"r") as f1:     
			for line in f1:
				img_name = txt_name.split('.')[0]
				img_full_path=src_img_dir+"/"+img_name+'.jpg'

				shutil.copy(img_full_path, new_img+"/"+"1_"+img_name+'.jpg')
				img=Image.open(img_full_path)
				width, height = img.size
				with open(os.path.join(txt_dir, txt_name),"r") as f2:
					xml_file = open((new_xml + '/' + '1_'+img_name + '.xml'), 'w')	  
					xml_file.write('<annotation>\n')
					xml_file.write('    <folder>JPEGImages</folder>\n')
					xml_file.write('    <filename>' + '1_'+ str(img_name)+'.jpg'+ '</filename>\n')
					xml_file.write('    <size>\n')
					xml_file.write('        <width>' + str(width) + '</width>\n')
					xml_file.write('        <height>' + str(height) + '</height>\n')
					xml_file.write('        <depth>3</depth>\n')
					xml_file.write('    </size>\n')

					for txt_line in f2:	

						info = txt_line.strip('\n').split(' ')
						xmin, ymin, xmax, ymax = info[0], info[1], info[2], info[3]
						#sub_category = int(category)
						# if category == 1:
							#x=category_location[1]   #class_label==1 or 2: x1，y1，w，h；
							#y=category_location[2]
							#w=category_location[3]
							#h=category_location[4]

						xml_file.write('    <object>\n')
						xml_file.write('        <name>' + 'phone' + '</name>\n')
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
						# else:
						# 	count += 1
						# 	print("current image is:",img_full_path)
					xml_file.write('</annotation>\n')
