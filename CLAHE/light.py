import cv2
import os
import numpy as np
from PIL import Image,ImageEnhance

def hisEqulColor(img):
    lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
    lab_planes=cv2.split(lab)
    clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    lab_planes[0]=clahe.apply(lab_planes[0])
    lab=cv2.merge(lab_planes)
    img=cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)
    return img
"""

def hisEqulColor(img):
    ycrcb =cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
    channels= cv2.split(ycrcb)
    cv2.equalizeHist(channels[0],channels[0])
    cv2.merge(channels,ycrcb)
    cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR,img)
    return img
"""

for i in range(1,661):
    if(os.path.isfile("/home/iis/darknet-master/data/mouss_seq1_origin/frame000"+(str(i).zfill(3))+".jpg")):
        img=cv2.imread("/home/iis/darknet-master/data/mouss_seq1_origin/frame000"+(str(i).zfill(3))+".jpg")
        eq=hisEqulColor(img)
        print("hi")
    #imgCLAHE=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    #eq = imgCLAHE.apply(img)
        cv2.imwrite("/home/iis/darknet-master/data/mouss_seq1/frame000"+(str(i).zfill(3))+".jpg",eq)
    else:
        continue
    #img=Image.open("/home/iis/darknet-master/data/mbari_seq0_origin/frame000"+(str(i).zfill(3))+".jpg")
    #contrast=ImageEnhance.Contrast(img)
    #contrast_img=contrast.enhance(2)
    #contrast_img.save("/home/iis/darknet-master/data/mbari_seq0/frame000"+(str(i).zfill(3))+".jpg")

#im=cv2.imread("/home/iis/darknet-master/contrast2.jpg")
#cv2.imshow("1",im)
#cv2.waitKey(0)
#img=cv2.imread("/home/iis/darknet-master/data/mbari_seq0_origin/frame000600.jpg")
#eq=hisEqulColor(img)
#cv2.imshow("2",eq)
#cv2.waitKey(0)

#cv2.imwrite("/home/iis/darknet-master/contrast1.jpg",eq)
#img=cv2.imread("/home/iis/darknet-master/data/mbari_seq0/frame000001.jpg",3)
#img=np.array(img)
#mean=np.mean(img)
#img=img-mean
#img=img*3+mean*1.4
#img=img/255. #<span style="white-space:pre"> </span>
#cv2.imshow("pic",img)
#cv2.waitKey()
#res=np.uint8(np.clip((1.68*img ),0,255))
#tmp=np.hstack((img,res))
#cv2.imshow('image',tmp)
#x=input("anything")
