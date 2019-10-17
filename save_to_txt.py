import os
import numpy as np

def create_txt(file_image):
    txt_path ='test.txt'
    txt = open(txt_path, 'w')
    for i in file_image:
        image_dir = os.path.join(str(i))
	image_name = image_dir.split('.')[0]
        #label_dir = os.path.join('./dataset/test_label/', str(j))
        txt.write(image_name+'\n')
        #txt.write(label_dir)

def read_file(path1):
    filelist1 = os.listdir(path1)
    file_image = np.array([file for file in filelist1 if file.endswith('.jpg')], dtype=object)
    #filelist2 = os.listdir(path2)
    #file_label = np.array([file for file in filelist2 if file.endswith('.png')], dtype=object)
    return file_image #, file_label


path1 = '/zhihui/CaltechDataset/output/img/test'
#path2 = './dataset/test_label/'

file_image = read_file(path1)
create_txt(file_image)

