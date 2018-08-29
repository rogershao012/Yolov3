import os
import json
from PIL import Image
from shutil import copyfile
path ="/home/iis/NewDownload/BeforeYolo/habcam_seq0"
files=os.listdir(path)
path2 ="/home/iis/NewDownload/COCO2xml/Annotations"
xml=os.listdir(path2)
count=0
for fil in files:
    for xm in xml:
        xmlfile=xm.strip(".xml")
        filfile=fil.strip(".png")
        if(xmlfile==filfile):
            copyfile("/home/iis/NewDownload/COCO2xml/Annotations/"+xm,"/home/iis/NewDownload/BeforeYolo/habcam_seq0/"+xm)
            print(count)
            count=count+1
