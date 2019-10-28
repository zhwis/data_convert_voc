#!/usr/bin/python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import os, argparse
import cv2
import xml.etree.cElementTree as ET

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--anno_dir", default="/opt/project/YOLO-master/darknet/results/annotation", help="dataset xml data root directory")
	parser.add_argument("--new_anno_dir", default="/opt/project/YOLO-master/darknet/results/new_tes_phone_cup", help="dataset xml data root directory")
	args = parser.parse_args()
	changeText = '2'
	for txt_name in os.listdir(args.anno_dir):  
		tree = ET.parse(os.path.join(args.anno_dir, txt_name))
		root = tree.getroot()
	
		for label in root.iter('name'):
			if label.text == "1":
				label.text = "phone"
			elif label.text == "4":
				label.text = "drink"
		tree.write(os.path.join(args.new_anno_dir, txt_name))

if __name__=='__main__':
	main()
