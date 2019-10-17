#! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image
import shutil
from scipy.io import loadmat
#img_Lists = glob.glob(src_img_dir + '\*.png')
 
# citypersons图像的标注位置
src_anno_dir = loadmat('/zhihui/CSP/data/citypersons/annotations/anno_val.mat')

# cityscapes图像的存储位置
src_img_dir = "/zhihui/CSP/data/cityscapes/leftImg8bit/val/"

#保存为VOC 数据集的原图和xml标注路径
new_img= "/zhihui/CSP/data/cityscapes/JPEGImages"
new_xml= "/zhihui/CSP/data/cityscapes/Annotations"

if not os.path.isdir(new_img):
    os.makedirs(new_img)
    
if not os.path.isdir(new_xml):
    os.makedirs(new_xml)   
    
a=src_anno_dir['anno_val_aligned'][0] 
    #处理标注文件

for i in range(len(a)):
    img_name=a[i][0][0][1][0].split('.')[0]   #frankfurt_000000_000294_leftImg8bit.png
    print("img name:", a[i][0][0][1])     
    dir_name=img_name.split('_')[0]
    img=src_img_dir+dir_name+"/"+img_name+'.jpg'
     
    shutil.copy(img, new_img+"/"+img_name+'.jpg')
    img=Image.open(img)
    width, height = img.size
    
    position=a[i][0][0][2]
    #print(position)
    #sys.exit()
    xml_name=img_name.split('.')[0]
    xml_file = open((new_xml + '/' + xml_name + '.xml'), 'w')
          
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>citysperson</folder>\n')
    xml_file.write('    <filename>' + str(img_name)+'.jpg'+ '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')
    
    for j in range(len(position)):
        category_location=position[j]  #[    1   947   406    17    40 24000   950   407    14    39]
        category=category_location[0]  # class_label =0: ignore regions 1: pedestrians 2: riders 3: sitting persons 4: other persons 5: group of people
       
        if category == 1 or category == 2:
            x=category_location[1]   #class_label==1 or 2: x1，y1，w，h；
            y=category_location[2]
            w=category_location[3]
            h=category_location[4]
               
       
            xml_file.write('    <object>\n')
            xml_file.write('        <name>' + 'person' + '</name>\n')
            xml_file.write('        <pose>Unspecified</pose>\n')
            xml_file.write('        <truncated>0</truncated>\n')
            xml_file.write('        <difficult>0</difficult>\n')
            xml_file.write('        <bndbox>\n')
            xml_file.write('            <xmin>' + str(x) + '</xmin>\n')
            xml_file.write('            <ymin>' + str(y) + '</ymin>\n')
            xml_file.write('            <xmax>' + str(x+w) + '</xmax>\n')
            xml_file.write('            <ymax>' + str(y+h) + '</ymax>\n')
            xml_file.write('        </bndbox>\n')
            xml_file.write('    </object>\n')
        else:
            continue
#             if 
            #if category == 1 or category ==2 or category ==3 category ==4 or category ==5:
        print("category:", category)
    xml_file.write('</annotation>\n')
