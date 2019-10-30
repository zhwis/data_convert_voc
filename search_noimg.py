# #! /usr/bin/python
# # -*- coding:UTF-8 -*-

import os
import shutil

def copy_nomath_img(src_img_dir, mod_img_dir, empty_img):
	if not os.path.isdir(empty_img):
		os.makedirs(empty_img)
	for name in os.listdir(src_img_dir):   
	    #img = name.split('.')[0]      
	    if not os.path.exists(os.path.join(mod_img_dir, "4_"+name)):
		shutil.copy(os.path.join(src_img_dir, name), empty_img+"/"+"4_"+name)

def del_nomatch_img(src_img_dir):
	for name in os.listdir(src_img_dir):   
	    img = name.split('.')[0]      
	    if not os.path.exists(os.path.join(new_xml, img+'.jpg')):
		print(img)
		os.remove(os.path.join(src_img_dir, name))

def main():
	src_img_dir = "/zhihui/DMS/state-farm-distracted-driver-detection/imgs/train/c6"
	new_xml = "/zhihui/DMS/darknet/results/new_add_phone/only_face_img"
	mod_img_dir = "/zhihui/DMS/darknet/results/drink/c6/JPEGImages"
	empty_img = "/zhihui/DMS/darknet/results/drink/c6/empty"
	
	copy_nomath_img(src_img_dir,mod_img_dir, empty_img)
	#del_nomatch_img(src_img_dir, new_xml, empty_img)

if __name__=='__main__':
     	main()

