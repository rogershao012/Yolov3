import os
import json
from PIL import Image
path ="/media/share33/Database/NOAA Fish Finding/Training Data Release/imagery/habcam_seq0_cut"
files=os.listdir(path)

with open("/media/share33/Database/NOAA Fish Finding/Training Data release/annotations/habcam_seq0_training.mscoco.json","r+") as f:
    allData = json.load(f)
    image = allData['images']
    data = allData["annotations"]
count=0
filenamelist=[]
for i in image:
    if(i['has_annots'] == True):
        for j in data:
            if(j["image_id"]==i["id"] and (j['roi_shape'] == "bbox" or j['roi_shape']=='line')):
                filenamelist.append(i['file_name'])
                print(count)
                count=count+1
count2=0
for fil in files:
    if(fil in filenamelist):
        im=Image.open(path+"/"+fil)
        im.save("/home/iis/NewDownload/BeforeYolo/habcam_seq0/"+fil)
        im.close()
        print(count2)
        count2=count2+1

print(count," ",count2)
