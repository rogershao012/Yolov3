import os
from PIL import Image
path ="/media/share33/Database/NOAA Fish Finding/Training Data Release/imagery/habcam_seq0"
files=os.listdir(path)
count=0
temp=[]
for fil in files:
    print(count)
    try:
        im=Image.open(path+"/"+fil)
        image_size=im.size
    #print("{}".format(image_size))
        x=0
        y=0
        w=1360
        h=1024
        region =im.crop((x,y,x+w,y+h))
        region.save("/media/share33/Database/NOAA Fish Finding/Training Data Release/imagery/habcam_seq0_cut/"+fil)
        count=count+1
        im.close()
    except:
        print(fil+" error")
        temp.append(fil)
        count=count+1
print("error:"+temp)

    
