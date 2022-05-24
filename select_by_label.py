import os
import glob

import numpy

data_path='D:/project/dataset/mix/test_gt/'
save_path='D:/project/dataset/mix/test_seal_gt/'
gt_list=os.listdir(data_path)
for gt_name in gt_list:
    with open(os.path.join(data_path,gt_name),'r',encoding='UTF-8') as f:
        lists=[]
        bbox=[]
        a=f.readlines()
        with open(os.path.join(save_path,gt_name),'w',encoding='UTF-8') as fid:
            for i in a:
                #i=numpy.array(i)
                i=i[:-1]
                print(i[-4:])
                if i[-4:]=='seal':
                    fid.write(i+'\n')
                #     for j in range(0,9):
                #         k=i.split(',')[j]
                #         lists.append(k)
                #     lists.append('\n')
                # bbox=[str(x) for x in lists]
                # bbox=','.join(bbox)
                # fid.write(bbox[:-1])
                # lists=[]

