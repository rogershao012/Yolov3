import json

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

def writeNum(Num):
    with open("COCO_train.json","a+") as f:
        f.write(str(Num))

# with open("instances_val2014.json","r+") as f:
#     data = json.load(f)
    # annData = data["annotations"]
    # print(annData[0])
    # for x in annData[0]:
    #     if(x == "image_id"):
    #         print(type(x))
    #         print(x+ ":" + str(annData[0][x]))
    #     if (x == "image_id" or x == "bbox" or x == "category_id"):
    #         print(x + ":" + annData[0][x])
    #     if (x == "image_id" or x == "bbox" or x == "category_id"):
    #         print(x+ ":" + annData[0][x])

# with open("test.json","w") as f:
#     json.dump(annData, f, ensure_ascii=False)

inputfile = []
inner = {}
##向test.json文件写入内容
with open("/media/share33/Database/NOAA Fish Finding/Training Data release/annotations/habcam_seq0_training.mscoco.json","r+") as f:
    allData = json.load(f)
    data = allData["annotations"]
    image = allData['images']
    print(data[1])
    print(len(data))
    print("read ready")

for i in data:
    if(i['category_id'] in classNum and (i['roi_shape'] == "bbox" or i['roi_shape']=='line')):
        for j in image:
            if(j["has_annots"]==True):
                if(i["image_id"]==j["id"]):
                    inner = {
                    "filename": str(j["file_name"]).zfill(6),
                    "name": className[i["category_id"]],
                    "bndbox":i["bbox"]
                    }
                    inputfile.append(inner)
print(type(inputfile))
print(inputfile[0])
#with open("COCO_train.json","a+") as f:
#    for hostdict in inputfile:
#        json.dump(hostdict,f)
#        f.write("\n")
inputfile = json.dumps(inputfile)
writeNum(inputfile)
