import os
import random
import shutil

txt_path='D:/temp_img/labels/'
img_id=open('D:/temp_img/val.txt').read().strip().split()
for img in img_id:
    txt=img.split('/')[-1].split('.')[0]
    txt_name=txt+'.txt'
    shutil.copy(os.path.join(img),os.path.join('D:/temp_img/images/','val'))
    shutil.copy(os.path.join(txt_path,txt_name), os.path.join('D:/temp_img/labels/', 'val'))