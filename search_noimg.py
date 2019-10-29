# #! /usr/bin/python
# # -*- coding:UTF-8 -*-

import os
src_img_dir = "/opt/project/YOLO-master/darknet/results/cup_phone_face/cup"
new_xml = "/opt/project/YOLO-master/darknet/results/cup_phone_face/new_ann"

for name in os.listdir(src_img_dir):   
    img = name.split('.')[0]      
    if not os.path.exists(os.path.join(new_xml, img+'.xml')):
        print(img)