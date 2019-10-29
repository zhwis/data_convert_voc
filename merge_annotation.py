# #! /usr/bin/python
# # -*- coding:UTF-8 -*-

import os
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element
from PIL import Image
import shutil

# caltech图像的存储位置
src_img_dir = "/opt/project/YOLO-master/darknet/results/cup_phone_face/cup"

#保存为VOC 数据集的原图和xml标注路径
new_img= "/opt/project/YOLO-master/darknet/results/cup_phone_face/new_img"
new_xml = "/opt/project/YOLO-master/darknet/results/cup_phone_face/new_ann"

cup_xml = "/opt/project/YOLO-master/darknet/results/cup_phone_face/Annotations-phone_cup"
face_xml = "/opt/project/YOLO-master/darknet/results/cup_phone_face/Annotations-face"
if not os.path.isdir(new_img):
	os.makedirs(new_img)
    
if not os.path.isdir(new_xml):
	os.makedirs(new_xml)   

face_count = 0
cup_count = 0
phone_count = 0

for txt_name in os.listdir(face_xml):
    if not os.path.exists(os.path.join(cup_xml, txt_name)):
        continue
    else:
        with open(os.path.join(face_xml, txt_name),"r") as f2:
            img_name = txt_name.split('.')[0]
            img_full_path=src_img_dir+"/"+img_name+'.jpg'
            shutil.copy(img_full_path, new_img+"/"+img_name+'.jpg')
            img=Image.open(img_full_path)
            width, height = img.size
            xml_file = open((new_xml + '/' + img_name + '.xml'), 'w')	  
            xml_file.write('<annotation>\n')
            xml_file.write('    <folder>JPEGImages</folder>\n')
            xml_file.write('    <filename>' + str(img_name)+'.jpg'+ '</filename>\n')
            xml_file.write('    <size>\n')
            xml_file.write('        <width>' + str(width) + '</width>\n')
            xml_file.write('        <height>' + str(height) + '</height>\n')
            xml_file.write('        <depth>3</depth>\n')
            xml_file.write('    </size>\n')

            tree = ET.parse(os.path.join(face_xml, txt_name))
            root = tree.getroot()

            for member in root.findall('object'):
                ### note: member[?] based on .xml
                xmin = int(member[1][0].text)    
                ymin = int(member[1][1].text)
                xmax = int(member[1][2].text)  
                ymax = int(member[1][3].text)
                class_name = member[0].text
                if class_name == "1":
                    face_count += 1
                xml_file.write('    <object>\n')
                xml_file.write('        <name>' + class_name + '</name>\n')
                xml_file.write('        <pose>Unspecified</pose>\n')
                xml_file.write('        <truncated>0</truncated>\n')
                xml_file.write('        <difficult>0</difficult>\n')
                xml_file.write('        <bndbox>\n')
                xml_file.write('            <xmin>' + str(xmin) + '</xmin>\n')
                xml_file.write('            <ymin>' + str(ymin) + '</ymin>\n')
                xml_file.write('            <xmax>' + str(xmax) + '</xmax>\n')
                xml_file.write('            <ymax>' + str(ymax) + '</ymax>\n')
                xml_file.write('        </bndbox>\n')
                xml_file.write('    </object>\n')

            tree = ET.parse(os.path.join(cup_xml, txt_name))
            root = tree.getroot()

            for member in root.findall('object'):
                ### note: member[?] based on .xml
                xmin = int(member[4][0].text)    
                ymin = int(member[4][1].text)
                xmax = int(member[4][2].text)  
                ymax = int(member[4][3].text)
                class_name = member[0].text
                if class_name == "2":
                    phone_count += 1
                elif class_name == "4":
                    cup_count += 1
                else:
                    pass
                xml_file.write('    <object>\n')
                xml_file.write('        <name>' + class_name + '</name>\n')
                xml_file.write('        <pose>Unspecified</pose>\n')
                xml_file.write('        <truncated>0</truncated>\n')
                xml_file.write('        <difficult>0</difficult>\n')
                xml_file.write('        <bndbox>\n')
                xml_file.write('            <xmin>' + str(xmin) + '</xmin>\n')
                xml_file.write('            <ymin>' + str(ymin) + '</ymin>\n')
                xml_file.write('            <xmax>' + str(xmax) + '</xmax>\n')
                xml_file.write('            <ymax>' + str(ymax) + '</ymax>\n')
                xml_file.write('        </bndbox>\n')
                xml_file.write('    </object>\n')

            xml_file.write('</annotation>\n')

for name in os.listdir(cup_xml):         
    if not os.path.exists(os.path.join(new_xml, name)):
        shutil.copy(os.path.join(cup_xml, name), new_xml+'/'+name)
print("face number:",face_count)
print("phone number:",phone_count)
print("cup number:",cup_count)
