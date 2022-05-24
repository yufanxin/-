import os

import numpy
import numpy as np
import codecs
import json
from glob import glob
import cv2
import shutil

def get_classes(classes_path):
    with open(classes_path, encoding='utf-8') as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names, len(class_names)
classes_path='my_classes.txt'
classes, _ = get_classes(classes_path)

json_path='D:\code\DP\object_dection\yolo\yolov5-6.1\datasets\images/'
files=glob(json_path+"*.json")
txt = 'D:\code\DP\object_dection\yolo\yolov5-6.1\datasets/' + 'train.txt'
txtfile = open(txt, 'a')
for file in files:
    with open(file,"r",encoding='utf-8') as f:
        data=json.load(f)
        txt = file.split('\\')[-1].replace('.json', '.txt')
        jpg_path = json_path + file.split('\\')[-1].replace('.json', '.jpg')
        # txt = 'D:\code\DP\object_dection\yolo\yolov5-6.1\datasets/labels/' + txt
        # txtfile = open(txt, 'a')
        txtfile.write(jpg_path+" ")
        for i in range(len(data['shapes'])):
            points=data['shapes'][i]['points']
        #points=data['shapes'][0]['points']
            xmin = points[0][0]
            ymin = points[0][1]
            xmax = points[1][0]
            ymax = points[1][1]
            label = data['shapes'][0]['label']
            # txt=file.split('\\')[-1].replace('.json','.txt')
            # jpg_path=json_path+file.split('\\')[-1].replace('.json','.jpg')
            # txt='D:\code\DP\object_dection\yolo\yolov5-6.1\datasets/labels/'+txt
            # txtfile=open(txt,'a')
            cls_id = classes.index(label)
            width=(xmax-xmin)/1912
            height=(ymax-ymin)/895
            center_x=float(xmax-int(width/2))/1912
            center_y=float(ymax-int(height/2))/895
            b=(center_x,center_y,width,height)
            txtfile.write(str(cls_id)+" "+" ".join([str(a) for a in b])+" ")
        txtfile.write("\n")
txtfile.close()
