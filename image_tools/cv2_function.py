import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path='D:\code/trick\image_tools/test11.jpg'
img=cv2.imread(image_path)
area1 = np.array([[58, 318], [55, 406]])
area2 = np.array([[76, 313], [70, 408]])

#cv2.fillPoly(img,[area1,area2],(255,255,255))
pology1=cv2.fillPoly(img,[area1,area2],(255,0,0))
pology2=pology1[:,:,np.newaxis]

plt.imshow(pology1)
plt.show()