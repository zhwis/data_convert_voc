#-*- coding: UTF-8 -*-
import os
import  random
import shutil
import numpy as np

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    return pathDir 
 
def divideTrainVal(source,dist):
    pic_name=eachFile(source)
    random.shuffle(pic_name)
    train_list = pic_name[0:int(0.7*len(pic_name))]
    validation_list = pic_name[int(0.7*len(pic_name)):]
    #test_list = pic_name[int(0.9*len(pic_name)):]
    for train_pic in train_list:              
        shutil.move(source+'/'+train_pic, dist+'/train/'+train_pic)   
    for validation_pic in validation_list:
        shutil.move(source+'/'+validation_pic, dist+'/val/'+validation_pic)
    
    #for test_pic in test_list:
    #    shutil.move(source+'/'+test_pic, dist+'/test/'+pos_or_neg+'/'+test_pic)
    return

def create_txt(dist, train_img, val_img):
    train_txt_path = os.path.join(dist, 'train.txt')
    val_txt_path = os.path.join(dist, 'val.txt')

    train_txt = open(train_txt_path, 'w')
    for i in train_img:
        image_dir = os.path.join(str(i))
	image_name = image_dir.split('.')[0]
        #label_dir = os.path.join('./dataset/test_label/', str(j))
        train_txt.write(image_name+'\n')
        #txt.write(label_dir)
    val_txt = open(val_txt_path, 'w')
    for i in val_img:
        image_dir = os.path.join(str(i))
	image_name = image_dir.split('.')[0]
        #label_dir = os.path.join('./dataset/test_label/', str(j))
        val_txt.write(image_name+'\n')

def read_file(train_path, val_path):
    filelist1 = os.listdir(train_path)
    train_img = np.array([file for file in filelist1 if file.endswith('.jpg')], dtype=object)
    filelist2 = os.listdir(val_path)
    val_img = np.array([file for file in filelist2 if file.endswith('.jpg')], dtype=object)
    return train_img, val_img
   
 
if __name__ == '__main__':
    img_path = '/zhihui/DMS/state-farm-distracted-driver-detection/face_phone_cup/img'
    dist = '/zhihui/DMS/state-farm-distracted-driver-detection/face_phone_cup/'
    divideTrainVal(img_path, dist)

    train_path = os.path.join(dist, 'train')
    val_path = os.path.join(dist, 'val')

    train_img, val_img = read_file(train_path, val_path)
    create_txt(dist, train_img, val_img)

