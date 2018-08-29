import json
#NOTICE! different dataset may need different setting 


#Remeber to Change ClassName and ClassNum pair to the coco json file
className = {
1:'Gastropoda',
2:'Osteroida',
3:'Cephalopoda',
4:'Decapoda',
5:'Aplousobranchia',
6:'NotPleuronectiformes',
7:'Perciformes',
8:"Fish",
9:"Rajiformes",
10:"NonLiving",
11:"Pleuronectiformes",
}

classNum = [1,2,3,4,5,6,7,8,9,10,11]

#store file
def writeNum(Num):
    with open("COCO_train.json","a+") as f:
        f.write(str(Num))

inputfile = []
inner = {}
##write content to json file
with open("/media/share33/Database/NOAA Fish Finding/Training Data release/annotations/habcam_seq0_training.mscoco.json","r+") as f:
    allData = json.load(f)
    data = allData["annotations"] #annotation part
    image = allData['images'] #images part
    print(data[1])  #check 
    print(len(data))  #check
    print("read ready")

for i in data:
    if(i['category_id'] in classNum and (i['roi_shape'] == "bbox" or i['roi_shape']=='line')): #We use only bbox and line(bbox) annotation
        for j in image:
            if(j["has_annots"]==True):
                if(i["image_id"]==j["id"]): #check if there are id both in annotation part and images part
                    inner = {
                    "filename": str(j["file_name"]).zfill(6),     #file_name is the same,zfill is in case of trouble
                    "name": className[i["category_id"]],
                    "bndbox":i["bbox"]
                    }
                    inputfile.append(inner)
print(type(inputfile)) #check
print(inputfile[0])  #check
#with open("COCO_train.json","a+") as f:
#    for hostdict in inputfile:
#        json.dump(hostdict,f)
#        f.write("\n")
inputfile = json.dumps(inputfile)
writeNum(inputfile)   #outputfile
