import time
import numpy as np
import cv2
import matplotlib.pyplot as plt

def CenterLableHotMap(img_width,img_height,c_x,c_y,sigma):
    X1=np.linspace(1,img_width,img_width)
    Y1=np.linspace(1,img_height,img_height)
    [X,Y]=np.meshgrid(X1,Y1)
    X=X-c_x
    Y=Y-c_y
    D2=X*X+Y*Y
    E2=2*sigma*sigma
    EXP=-D2/E2
    heatmap=np.exp(EXP)
    return heatmap


# Compute gaussian kernel
def CenterGaussianHeatMap(img_height, img_width, c_x, c_y, variance):
    gaussian_map = np.zeros((img_height, img_width))
    for x_p in range(img_width):
        for y_p in range(img_height):
            dist_sq = (x_p - c_x) * (x_p - c_x) + \
                      (y_p - c_y) * (y_p - c_y)
            exponent = dist_sq / 2.0 / variance / variance
            gaussian_map[y_p, x_p] = np.exp(-exponent)
    return gaussian_map

img_file='005281.jpg'
img=cv2.imread(img_file)
img=img[:,:,::-1]

height, width,_ = np.shape(img)
cy, cx = height/2.0, width/2.0

heatmap1 = CenterLableHotMap(width, height, cx, cy, 21)
heatmap2=CenterGaussianHeatMap(height,width,cx,cy,21)
plt.subplot(1,2,1)
plt.imshow(heatmap1)
plt.subplot(1,2,2)
plt.imshow(heatmap2)
plt.show()

