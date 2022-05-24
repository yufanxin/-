import cv2
import numpy as np

def rotateAnticlockwise90(img_file): #逆时针旋转90度
    img=cv2.imread(img_file)
    trans_img=cv2.transpose(img)
    img90=cv2.flip(trans_img,0) #参数可以设置为1，0，-1，分别对应着水平翻转、垂直翻转、水平垂直翻转
    cv2.imshow("rotate",img90)
    cv2.waitKey(0)
    return img90

def totateAntiClockWise90ByNumpy(img_file):  # np.rot90(img, 1) 逆时针旋转90度
    img=cv2.imread(img_file)
    img90=np.rot90(img,1)
    cv2.imshow("rotate",img90)
    cv2.waitKey(0)
    return img90

#rotateAnticlockwise90('C:/Users\YFX\Pictures\icon/333.jpg')
totateAntiClockWise90ByNumpy('C:/Users\YFX\Pictures\icon/333.jpg')
# sourceImage=cv2.resize(sourceImage,(618,618))
# # 显示原图片上
# cv2.imshow("sourceImage", sourceImage)
# # 转置阵图片
# transposedImage = cv2.transpose(sourceImage)
# # 显示转置阵后的图片
# cv2.imshow("transposedImage", transposedImage)
# # 实现沿X轴方向的镜像图片
# flipedImageX = cv2.flip(transposedImage, 0)
# # 显示沿X轴方向的镜像图片
# cv2.imshow("flipedImageX", flipedImageX)
# # 实现沿Y轴方向的镜像图片
# flipedImageY = cv2.flip(transposedImage, 1)
# # 显示沿Y轴方向的镜像图片
# cv2.imshow("flipedImageY", flipedImageY)
# cv2.waitKey(0)
