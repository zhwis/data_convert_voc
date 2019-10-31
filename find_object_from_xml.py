#!/usr/bin/python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import os, argparse
import cv2
import xml.etree.cElementTree as ET
import re
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--anno_dir", default="/zhihui/DMS/state-farm-distracted-driver-detection/face_phone_cup/annotation", help="dataset xml data root directory")
	parser.add_argument("--val_dir", default="/zhihui/DMS/state-farm-distracted-driver-detection/face_phone_cup/val", help="dataset xml data root directory")
	args = parser.parse_args()
	count = 0
	for txt_name in os.listdir(args.val_dir):
	        matchObj = re.match("^4.*", txt_name)
		if matchObj is not None: 	
			target_name = matchObj.group()
			image = cv2.imread(os.path.join(args.val_dir, target_name))
			name = target_name.split('.')[0]
			tree = ET.parse(os.path.join(args.anno_dir, name+'.xml'))
			root = tree.getroot()
			count += 1
			#for label in root.iter('name'):
			#	if label.text == "face":
			for member in root.findall('object'):
				### note: member[?] based on .xml
				xmin = int(member[4][0].text if len(member)>4 else member[1][0].text)    
				ymin = int(member[4][1].text if len(member)>4 else member[1][1].text) 
				xmax = int(member[4][2].text if len(member)>4 else member[1][2].text)  
				ymax = int(member[4][3].text if len(member)>4 else member[1][3].text) 
				class_name = member[0].text 
				print(target_name)
				print("box value:",xmin,ymin,xmax,ymax)
				cv2.rectangle(image, (xmin, ymin), (xmax, ymax),(0, 0, 255), 2)
				cv2.putText(image, class_name, (xmin+15, ymin+15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
				cv2.namedWindow("result", cv2.WINDOW_NORMAL)
				#cv2.resizeWindow("result", 640, 480)
				cv2.imshow("result", image)

			if cv2.waitKey(0) & 0xFF == ord('q'):
				break		
					
		else:
			continue

	cv2.destroyAllWindows()
	print(count)

if __name__=='__main__':
	main()
