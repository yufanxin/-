# -*- coding: utf-8 -*-
import glob
import os.path
import json

def jsonTotxt(jsonfile):
    filename = os.path.split(jsonfile)[1].split('.')[0]
    savefile = os.path.join("C:/Users/YFX/Desktop/test/txt/test/", filename + '.txt')
    # read json
    # setting = []
    with open(jsonfile, 'r') as f:
        b = f.read()
        # b = b.encode("utf-8-sig")
        data = json.loads(b)
    # print(data)
    with open(savefile, "a", encoding='utf-8') as f:
        for coordict in data['shapes']:
            coordlist = coordict['points']
            for point in coordlist:
                f.write(str(point).replace('[', '').replace(']', '') + ',')
            f.write(coordict['label'] + '\n')

INPUT_PATH = 'D:/project/dataset/wzw_datasets/loc/test/'   # "F:/Pycharm/Project/DBNet.pytorch/datasets/新建文件夹"
json_glob = os.path.join(INPUT_PATH, '*.json')
json_lists = glob.glob(json_glob)
for json_list in json_lists:
    jsonTotxt(json_list)