import os
import re
import cv2
import sys
#the source folder that you will read the .jpg and .xml from
src0="/home/iis/NewDownload/BeforeYolo/habcam_seq0"
#the destation folder that you will save the .jpg files and .txt files, which are rename and transformed
dst0='/home/iis/NewDownload/AfterYolo/habcam_seq0'
#the num of the class that your cutting picture described in your .xml file belong to
voc_name0='/home/iis/NewDownload/BeforeYolo/habcam_seq0.names'
if __name__=='__main__':
    if len(sys.argv)<4:
        print('yolo-voc program need 5 argv.you must input command like\n   python 123.py [start_num] [source folder name] [deststion folder name] [voc name file]')
    else:
        p=int(sys.argv[1])
        src=sys.argv[2]+'/'
        dst=sys.argv[3]+'/'
        if len(sys.argv)>4:
            voc_name=sys.argv[4]
            voc_flag=True
        else:
            voc_name=''
            voc_flag=False
        '''src=input('please input the path of source:\n')
        if src=='':
            src=src0
            dst=dst0
            voc_name=voc_name0
        else:
            dst=input('please input the path of destination:\n')
            if dst=='':
                dst = dst0
                voc_name = voc_name0
            else:
                voc_name = input('please input the class_name file:\n')
                if dst=='':
                    voc_name = voc_name0'''
        listd=os.listdir(src)
        txt=re.compile(r'.*(xml)')
        listdir=[]
        for i in listd:
            if re.findall(txt,i):
                listdir.append(i)
        #listdir is filename of xml
        cc=r'<xmin>(.*)</xmin>'
        ffilename=re.compile(r'<filename>(.*)</filename>')
        xxmin=re.compile(r'<xmin>(.*)</xmin>')
        yymin=re.compile(r'<ymin>(.*)</ymin>')
        xxmax=re.compile(r'<xmax>(.*)</xmax>')
        yymax=re.compile(r'<ymax>(.*)</ymax>')
        wwidth=re.compile(r'<width>(.*)</width>')
        hheight=re.compile(r'<height>(.*)</height>')
        nname=re.compile(r'<name>(.*)</name>')
        if voc_flag==True:
            f=open(voc_name)
            listname=f.read()
            #listname is species' name
            f.close()
        
        p=0
        for i in listdir:
            i_file=open(src+i,'r')
            i_content=i_file.read()
            i_file.close()
            #print(i_content)
            name = (re.findall(nname, i_content)[0])
            names=re.findall(nname,i_content)
            xmin=re.findall(xxmin,i_content)
            ymin=re.findall(yymin,i_content)
            xmax=re.findall(xxmax,i_content)
            ymax=re.findall(yymax,i_content)
            filename=(re.findall(ffilename,i_content)[0])
            filename0=filename.split(".")[0]
            txtname0 = dst  + str(filename).rstrip(".png") + ".txt"
            #txtname0 = dst + "frame" +str(int(filename0)).zfill(6) + '.txt'
            f = open(txtname0, 'w')
            del names[0]
            for j in range(0,len(names)):
                if voc_flag==True:
                    index = listname.index(names[j])
                if(names[j]=="Gastropoda"):
                    index = 0
                elif(names[j]=="Aplousobranchia"):
                    index = 2
                elif(names[j]=="Cephalopoda"):
                    continue
                    index = 2
                elif(names[j]=="Decapoda"):
                    continue
                    index = 3
                elif(names[j]=="Osteroida"):
                    index = 1
                elif(names[j]=="NotPleuronectiformes"):
                    index = 3
                elif(names[j]=="Perciformes"):
                    continue
                    index = 6
                elif(names[j]=="Fish"):
                    continue
                    index = 7
                elif(names[j]=="Rajiformes"):
                    index = 4
                elif(names[j]=="NonLiving"):
                    index = 5
                elif(names[j]=="Pleuronectiformes"):
                    index = 6
                else:
                    index = 0

                width=int(float(re.findall(wwidth,i_content)[0]))
                height=int(re.findall(hheight,i_content)[0])
                Newxmin=int(float(xmin[j]))
                Newymin=int(float(ymin[j]))
                Newxmax=int(float(xmax[j]))
                Newymax=int(float(ymax[j]))



            #txtname=dst+i
            #txtname0=txtname.replace('xml','txt')

                if j!=0:
                    f.write('\n')
                f.write(str(index)+' '+'%0.4f'%((float(Newxmin)+float(Newxmax))/float(width)/2)+' '+'%0.4f'%((float(Newymin)+float(Newymax))/float(height)/2)+' '+'%0.4f'%(float(Newxmax-Newxmin)/float(width))+' '+'%0.4f'%(float(Newymax-Newymin)/float(height)))
            f.close()
            imgsource=src+i
            imgname0 = imgsource.replace('xml', 'png')
            img=cv2.imread(imgname0)
            #print(img)

            if img is None:
                imgname0=imgname0.replace('png','JPG')
                img = cv2.imread(imgname0)
            if img is None:
                imgname0 = imgname0.replace('JPG', 'jpg')
                img = cv2.imread(imgname0)
            imgdst = dst  + str(filename).rstrip(".png")+".jpg"
            #imgdst=dst+"frame"+str(filename0).zfill(6)+'.jpg'
            #imgname1 = imgdst.replace('xml', 'jpg')
            cv2.imwrite(imgdst,img)
            p+=1

