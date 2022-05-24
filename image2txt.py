import os
from glob import iglob as glob

data_path='D:/publish/centernet-pytorch-main/dianchang/train1.txt'
imgs_root = 'D:/publish/centernet-pytorch-main/dianchang/train/img'
labels_root = 'D:/publish/centernet-pytorch-main/dianchang/train/gt'
imgs_path = os.listdir(imgs_root)
labels_path = os.listdir(labels_root)

for i in labels_path:
    label_list = []
    total_list = []
    img_path = os.path.join(imgs_root,i.replace('txt','jpg'))
    total_list.append(img_path)
    total_list.append('\t')
    label_path = os.path.join(labels_root,i)
    for line in open(label_path,'r'):
        label_list.append(line[:-1])
    for j in label_list:
        total_list.append(j)
        total_list.append('\t')
    with open(data_path,'a') as f:
        for i in total_list[:-1]:
            f.write(i)
        f.write('\n')







# def img2txt(image_root,txt_root):
#     image_path_list=glob(image_root+r'\*.jpg')
#
#     for image_path in image_path_list:
#         image_name=image_path.split('\\')[1].split('.')[0]
#         f=open(txt_root+'/'+image_name+'.txt')
#         label=f.readlines()
#         with open(data_txt, 'w') as f:
#             f.write(image_path)
#             for i in range(len(label)):
#                 label[i]=label[i].strip('\n')
#                 print(label[i])
#                 temp=[]
#                 temp.append(int(float(tem for tem in label[i])))
#                 print(temp)
#                 f.write(label)

# img2txt('D:/publish/centernet-pytorch-main/dianchang/train/img','D:/publish/centernet-pytorch-main/dianchang/train/gt')