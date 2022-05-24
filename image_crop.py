import numpy as np
import cv2 as cv
from glob import iglob as glob
from xml.etree import ElementTree as ET
import os

def image_crop(xml_root, image_root, dst_root):
    xml_path_list = glob(xml_root + r'\*.xml')

    for xml_path in xml_path_list:
        xml = ET.parse(xml_path)
        for object in xml.findall('object'):
            xmin = object.find('bndbox').find('xmin').text
            ymin = object.find('bndbox').find('ymin').text
            xmax = object.find('bndbox').find('xmax').text
            ymax = object.find('bndbox').find('ymax').text

            image_name = xml_path.split('\\')[-1].split('.')[0]
            image_path = os.path.join(image_root, image_name + '.jpg')
            image = cv.imdecode(np.fromfile(image_path, np.uint8), cv.IMREAD_UNCHANGED)

            image_dst = image[int(ymin):int(ymax), int(xmin):int(xmax), :]
            image_dst_path = os.path.join(dst_root, image_name+ '.jpg')
            cv.imencode('.jpg', image_dst)[1].tofile(image_dst_path)
    print('Done!')

if __name__ == '__main__':
    image_crop(r'D:\project\dataset\car\test\label',
               r'D:\project\dataset\car\test\image',
               r'D:\code\OCR\crnn\data\car_test\image')
