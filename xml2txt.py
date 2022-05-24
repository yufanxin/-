import xml.etree.ElementTree as ET
from os import getcwd
import glob
#sets = ['train', 'val', 'test']


def convert_annotation(image_id, list_file):
    in_file = open('D:/project/dataset/car/test/label/%s.xml' % (image_id), encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = 0
        if obj.find('difficult') != None:
            difficult = obj.find('difficult').text

        cls = obj.find('name').text
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),int(xmlbox.find('ymin').text),int(xmlbox.find('xmax').text),
             int(xmlbox.find('ymax').text),int(xmlbox.find('xmin').text),int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + cls+'\n')


#wd = getcwd()

path=glob.glob('D:\project\dataset\lieche/test_gt_xml/*.xml')
for i in path:
    image_name = i.split('\\')[-1].split('.')[0]
    list_file = open('D:\project\dataset\lieche/test_gt_txt/%s.txt' % (image_name), 'w')
    #list_file.write('D:\project\新箱号识别\container/Image/%s.jpg' % (image_id))
    convert_annotation(image_name, list_file)
    list_file.write('\n')
    list_file.close()
