import os
org_path='D:/project/OCR/DBNet/datasets/dianchang/test/gt/'
dst_path='D:/project/OCR/DBNet/datasets/dianchang/test/gt1/'

label_list=os.listdir(org_path)
for txt_name in label_list:
    with open(os.path.join(org_path,txt_name),'r',encoding='utf-8') as f:
        a=f.readlines()
        arry=[]
        list=[]
        with open(os.path.join(dst_path,txt_name), 'w') as fid:
            for i in a:
                for j in range(0,9):
                    k=i.split(',')[j]
                    if j !=8:
                        k=int(float(k))
                    else:
                        k=k
                    list.append(k)
                bbox = [str(x) for x in list]
                bbox = ','.join(bbox)
                fid.write(bbox)
                list=[]
