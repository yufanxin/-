import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
image_path='test.jpg'
image=cv2.imread(image_path)
image=cv2.resize(image,(960,540))
for i in range(60,120):
    for j in range(0,300):
        image[j,i]=(0,0,0)
plt.imshow(image)
plt.show()