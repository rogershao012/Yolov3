#original from
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 10:05
# @Author  : He Hangjiang
# @Site    : 
# @File    : creatXML.py
# @Software: PyCharm

import xml.dom
import xml.dom.minidom
import os
# from PIL import Image
import cv2
import json

# xml format

#Remember to change the PATH
_IMAGE_PATH= '/media/share33/Database/NOAA Fish Finding/Training Data Release/imagery/habcam_seq0'

#some information you can change
_INDENT= ''*4
_NEW_LINE= '\n'
_FOLDER_NODE= 'habcam_seq0'
_ROOT_NODE= 'annotation'
_DATABASE_NAME= 'NOAA Fish Finding'
_ANNOTATION= 'habcam_seq0'
_AUTHOR= 'hahaha'
_SEGMENTED= '0'
_DIFFICULT= '0'
_TRUNCATED= '0'
_POSE= 'Unspecified'

_ANNOTATION_SAVE_PATH= 'Annotations'

# encapsulation create node
def createElementNode(doc,tag, attr):  # create a node
    element_node = doc.createElement(tag)

    # create a text node
    text_node = doc.createTextNode(attr)

    # make text node being element node's Child node
    element_node.appendChild(text_node)

    return element_node

# encapsulation add node
def createChildNode(doc,tag, attr,parent_node):

    child_node = createElementNode(doc, tag, attr)

    parent_node.appendChild(child_node)


#Object node
def createObjectNode(doc,attrs):

    object_node = doc.createElement('object')

    createChildNode(doc, 'name', attrs['name'],
                    object_node)

    createChildNode(doc, 'pose',
                    _POSE, object_node)

    createChildNode(doc, 'truncated',
                    _TRUNCATED, object_node)

    createChildNode(doc, 'difficult',
                    _DIFFICULT, object_node)

    bndbox_node = doc.createElement('bndbox')

    createChildNode(doc, 'xmin', str(int(attrs['bndbox'][0])),
                    bndbox_node)


    createChildNode(doc, 'ymin', str(int(attrs['bndbox'][1])),
                    bndbox_node)

    createChildNode(doc, 'xmax', str(int(attrs['bndbox'][0]+attrs['bndbox'][2])),
                    bndbox_node)

    createChildNode(doc, 'ymax', str(int(attrs['bndbox'][1]+attrs['bndbox'][3])),
                    bndbox_node)

    object_node.appendChild(bndbox_node)

    return object_node

# Write documentElement into XML doc
def writeXMLFile(doc,filename):

    tmpfile =open('tmp.xml','w')

    doc.writexml(tmpfile, addindent=''*4,newl = '\n',encoding = 'utf-8')

    tmpfile.close()

    # delete annotation

    fin =open('tmp.xml')
    # print(filename)
    fout =open(filename, 'w')
    # print(os.path.dirname(fout))

    lines = fin.readlines()

    for line in lines[1:]:

        if line.split():
            fout.writelines(line)

        # new_lines = ''.join(lines[1:])

        # fout.write(new_lines)

    fin.close()

    fout.close()


if __name__ == "__main__":
    ##read picture remember to updata
    img_path = "/media/share33/Database/NOAA Fish Finding/Training Data Release/imagery/habcam_seq0"
    fileList = os.listdir(img_path)
    if fileList == 0:
        os._exit(-1)
    ann_data=[]
    with open("COCO_train.json", "r") as f:
        ann_data = json.load(f)

    current_dirpath = os.path.dirname(os.path.abspath('__file__'))

    if not os.path.exists(_ANNOTATION_SAVE_PATH):
        os.mkdir(_ANNOTATION_SAVE_PATH)

    # if not os.path.exists(_IMAGE_COPY_PATH):
    #     os.mkdir(_IMAGE_COPY_PATH)

    for imageName in fileList:

        saveName= imageName.strip(".png")
        saveName= saveName.strip("frame")

        #xml_file_name = os.path.join(_ANNOTATION_SAVE_PATH, ("frame"+saveName + '.xml'))
        xml_file_name = os.path.join(_ANNOTATION_SAVE_PATH, (saveName + '.xml'))
        # with open(xml_file_name,"w") as f:
        #     pass

        img=cv2.imread(os.path.join(img_path,imageName))
        print(os.path.join(img_path,imageName))
        # cv2.imshow(img)
        try:
                height,width,channel=img.shape
                print(height,width,channel)
        except:
	        print(saveName+"fail")

        my_dom = xml.dom.getDOMImplementation()

        doc = my_dom.createDocument(None,_ROOT_NODE,None)

        #find node
        root_node = doc.documentElement

        #folder node

        createChildNode(doc, 'folder',_FOLDER_NODE, root_node)

        #filename node

        createChildNode(doc, 'filename',saveName+'.png',root_node)

        #source node

        source_node = doc.createElement('source')

        #source node

        createChildNode(doc, 'database',_DATABASE_NAME, source_node)

        createChildNode(doc, 'annotation',_ANNOTATION, source_node)

        createChildNode(doc, 'image','flickr', source_node)

        createChildNode(doc, 'flickrid','NULL', source_node)

        root_node.appendChild(source_node)

        #owner node

        owner_node = doc.createElement('owner')

        #owner childnode

        createChildNode(doc, 'flickrid','NULL', owner_node)

        createChildNode(doc, 'name',_AUTHOR, owner_node)

        root_node.appendChild(owner_node)

        #sizenode

        size_node = doc.createElement('size')
        #if your training and width not the same size modify here(ex:cutted habcam)
        createChildNode(doc, 'width',str(width), size_node)

        createChildNode(doc, 'height',str(height), size_node)

        createChildNode(doc, 'depth',str(channel), size_node)

        root_node.appendChild(size_node)

        # segmented node

        createChildNode(doc, 'segmented',_SEGMENTED, root_node)
        count=0
        for ann in ann_data:
            if((saveName+".png")==ann["filename"]):
                # object node
                object_node = createObjectNode(doc, ann)
                root_node.appendChild(object_node)
                count=count+1
            else:
                continue

        # construct xml filename

        print(xml_file_name)

        #write in document
        #
        if(count>0):
            writeXMLFile(doc, xml_file_name)
