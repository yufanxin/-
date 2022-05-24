import os

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

# train or test
path = 'D:/project/OCR/DBNet/datasets/test/img'   #修改
lines = []
for root, dicts, files in os.walk(path):
    # print(dicts)
    print(files)

    for index, file in enumerate(files, 1):
        img = file
        txt = file.replace('.jpg','.txt')
        lines.append('D:/project/OCR/DBNet/datasets/test/img/' + img + '\t' + 'D:/project/OCR/DBNet/datasets/test/gt/' + txt + '\n') #修改

f=open('D:\project\OCR\DBNet\datasets\\test.txt', 'w')   #修改
for line in lines:
    f.write(line)
f.close()