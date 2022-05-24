import cv2
import numpy as np
import matplotlib.pyplot as plt

#变换前后四个点求变换矩阵M
img=cv2.imread('test.jpg')
rows,cols=img.shape[:2]
img=img[:,:,[2,1,0]]
pts1 = np.float32([[56,65],[238,52],[28,237],[239,240]])
pts2 = np.float32([[0,0],[200,0],[0,200],[200,200]])

M=cv2.getPerspectiveTransform(pts1,pts2)
res=cv2.warpPerspective(img,M,(200,200))
plt.subplot(121)
plt.imshow(img)
plt.show()
plt.subplot(122)
plt.imshow(res)
plt.show()