import cv2

#帧数间隔截取视频帧
cap=cv2.VideoCapture("D:\code\MOT\yolov5-deepsort/video/test143.mp4")
c=1
framerate=10

while(True):
    ret,frame=cap.read()
    if ret:
        if (c%framerate==0):
            print("开始截取视频第："+str(c)+"帧")
            #截取帧到本地
            cv2.imwrite("D:/temp_img/1/"+str(c)+'.jpg',frame)
        c=c+1
        cv2.waitKey(0)
    else:
        print("所有帧已保存完成")
        break
cap.release()