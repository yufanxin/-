import shutil
import os
import random

img_path='D:/temp_img/images_ori/'
txt_path='D:/temp_img/labels/'
copy_to_path='D:/temp_img/images/'

txt_list=os.listdir(txt_path)
for txt in txt_list:
    img=txt.replace('.txt','.jpg')
    shutil.copy(os.path.join(img_path,img),os.path.join(copy_to_path,img))
    print(img)