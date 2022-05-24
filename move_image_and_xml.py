import shutil
import os
import random
import glob
import os.path

ori_dir='F:/yfx/车牌/过道/'
dst_image_dir='D:/project/dataset/car/train/image/'
dst_xml_dir='D:/project/dataset/car/train/label/'

image_glob=os.path.join(ori_dir,'*.jpg')
image_list=glob.glob(image_glob)
for image in image_list:
    image_name=image.split('\\')[-1]
    xml_name=image_name.replace('.jpg','.xml')
    xml=image.replace('.jpg','.xml')
    shutil.copy(os.path.join(image),os.path.join(dst_image_dir,image_name))
    shutil.copy(os.path.join(xml),os.path.join(dst_xml_dir,xml_name))

