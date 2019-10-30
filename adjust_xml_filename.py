# #! /usr/bin/python
# # -*- coding:UTF-8 -*-

import os
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element
from PIL import Image
import shutil

done_xml = "/zhihui/DMS/state-farm-distracted-driver-detection/face_phone_cup/done"
adjust_xml = "/zhihui/DMS/state-farm-distracted-driver-detection/face_phone_cup/adjust_xml_filename"

for txt_name in os.listdir(adjust_xml):         
	name = txt_name.split('.')[0]
	tree = ET.parse(os.path.join(adjust_xml, txt_name))
	root = tree.getroot()
	node = root.find('filename')
	node.text = name + '.jpg'
	tree.write(os.path.join(done_xml, txt_name), encoding="utf-8", xml_declaration=True)
	# done_xml can be written to original path
