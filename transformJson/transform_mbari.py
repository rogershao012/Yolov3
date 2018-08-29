#addFrom
#mouss1=55661
#mbari1=55516
#mouss2=56080
#mouss3=56800
#mouss4=57283
#mouss5=59565
#habcam=3177
import json

startNumber=55516
inputName="result_mbari1.txt"

fp=open(inputName,"r")
lines=fp.readlines()
fp.close()
image_id=0
count=0
finalList=[]
d={}

for i in lines:
    new=i.split(" ")
    if(len(new[0])>1):
        count=image_id
        addnumber=int(new[0].lstrip("frame").strip(".jpg")) #.format and "habcam" have to modify
        image_id=startNumber+addnumber
        continue
    else:
        try:
            d["image_id"]=int(count)
            d["category_id"]=str(new[0])
            d["bbox"]=[float(new[2]),float(new[3]),float(new[4]),float(new[5].strip("\n"))]
            d["score"]=float(new[1])      
            finalList.append(d)
        except:
            print("strange")
with open("mbari1.mscoco.json","w") as outfile:
    json.dump(finalList,outfile)


