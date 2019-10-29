#!/usr/bin/python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import os, argparse
import cv2
import xml.etree.cElementTree as ET
#img_path = "/zhihui/CSP/data/cityscapes/JPEGImages/"
#txt_path = "/zhihui/CSP/data/cityscapes/Annotations/"
def main():
	parser = argparse.ArgumentParser()
    	parser.add_argument("--img_dir", default="/zhihui/CaltechDataset/output_pull_path/frame/set02/frame", help="dataset img data root directory")
    	parser.add_argument("--anno_dir", default="/zhihui/CaltechDataset/output_pull_path/annotation/annotations/set02/bbox", help="dataset xml data root directory")
	args = parser.parse_args()

	sub_img = os.listdir(args.img_dir)
	for img_name in sub_img:
	    full_path = os.path.join(args.img_dir, img_name)
	    image = cv2.imread(full_path)
	    name = img_name.split('.')[0]
	    tree = ET.parse(os.path.join(args.anno_dir, name+'.xml'))
	    root = tree.getroot()
	    print("image name:", root.find('filename').text)
	    for member in root.findall('object'):
		### note: member[?] based on .xml
		xmin = int(member[4][0].text)    
		ymin = int(float(member[4][1].text)) 
		xmax = int(member[4][2].text)  
		ymax = int(member[4][3].text)
		class_name = member[0].text    
		print("box value:",xmin,ymin,xmax,ymax)
		cv2.rectangle(image, (xmin, ymin), (xmax, ymax),(0, 0, 255), 2)
		cv2.putText(image, class_name, (xmin+15, ymin+15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
		cv2.namedWindow("result", cv2.WINDOW_NORMAL)
		#cv2.resizeWindow("result", 640, 480)
		cv2.imshow("result", image)

	    if cv2.waitKey(0) & 0xFF == ord('q'):
		break
	cv2.destroyAllWindows()

def read_txt():
    f2 = open('./annotation_small_box.txt','r+')
    names = f2.readlines()
    for name in names:
    # for name in box:
	name = name.strip("\n")
	img_name = name.strip(".txt")
	path = img_path+ '/'+ img_name + '.jpg'
	with open(os.path.join(txt_path, name),'r') as f:
	    for line in f:
		xmin = int(line.split(' ')[1])
		ymin = int(line.split(' ')[2])
		xmax = int(line.split(' ')[3])
		ymax = int(line.split(' ')[4])

if __name__=='__main__':
     	main()





	

