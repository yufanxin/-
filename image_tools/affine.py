import cv2
import numpy as np
import matplotlib.pyplot as plt

#根据变换前后三个点来自动求解变换矩阵M
img=cv2.imread('test.jpg')  #cv2读取格式为bgr
rows,cols=img.shape[0:2]
#调整格式为rgb
img=img[:,:,[2,1,0]]
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M=cv2.getAffineTransform(pts1,pts2)

#第三个参数，变换后图像的大小
res=cv2.warpAffine(img,M,(rows,cols))

plt.subplot(121)
plt.imshow(img)
plt.show()
plt.subplot(122)
plt.imshow(res)
plt.show()