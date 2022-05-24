#图片批量resize
import cv2
import glob
import os

image_path="D:/temp_img/1/*.jpg" #原始图片路径
output_path="D:/temp_img/1_image/" #修改后的保存路径
count=0
for jpgfile in glob.glob(image_path):
    count+=1
    image=cv2.imread(jpgfile)
    image=cv2.resize(image,(1280,720),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(output_path,os.path.basename(jpgfile)),image)
    print("save%d"%count)
print("resized finished!")
