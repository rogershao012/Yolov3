import os
import re
import sys
src='/home/iis/darknet/x64/data/obj'
path='/home/iis/darknet/x64/data/obj'
if __name__=='__main__':
    if len(sys.argv)<2:
        print('piclist2txt program need 1 argv.you must input command like\n   python 123.py [source folder name] [changed path]')
    else:
        src=sys.argv[1]+'/'
        if len(sys.argv)>2:
            path=sys.argv[2]+'/'
        else:
            path=src
        filedir=os.listdir(src)
        imgfile=re.compile(r'.*(jpg|jpeg|JPEG|png)')
        listdir=[]
        for i in filedir:
            if re.match(imgfile,i):
                listdir.append(i)
        #print(listdir)
        f=open(src+'train.txt','w')
        for i in listdir:
            print(path+i)
            want=i.split(".")[0]
	    
            #f.write(dst+i+'\n')
            f.write(path+i+'\n')
            #f.write(path+want+".xml"+'\n')
            #f.write((i).replace('.jpg','') + '\n')
        f.close()
