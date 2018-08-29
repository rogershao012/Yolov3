# Yolov3
Yolov3 instruction for handover
original project from 
https://github.com/AlexeyAB/darknet

<h3>Following is some introductions and files base on the repository:</h3>
<ul>
<li><b>Finalweights Folder</b> -> <b>Introduce of my training setting and weights file</b></li>
<li><b>COCO2YOLO Folder</b> -> <b>Change COCO format to YOLO format and provide tool to show file path</b></li>
</ul>

<h3>STEPS:</h3>
<br><b> 1.Download the original project from https://github.com/AlexeyAB/darknet and check the Requires </b></br>
<br><b> 2.Go to its dictionary and open Makefile to change as following and do make in the directory</b></br>
<br>(1)"GPU=1" to build with CUDA to accelerate by using GPU (CUDA should be in `/usr/local/cuda`)
<br>(2)"CUDNN=1" to build with cuDNN v5-v7 to accelerate training by using GPU (cuDNN should be in `/usr/local/cudnn`)</br>
<br>(3)"CUDNN_HALF=1" to build for Tensor Cores (on Titan V / Tesla V100 / DGX-2 and later) speedup Detection 3x, Training 2x</br>
<br>(4)"OPENCV=1" to build with OpenCV 3.x/2.4.x - allows to detect on video files and video streams from network cameras or web-cams</br>
<br>(5)"DEBUG=1" to bould debug version of Yolo</br>
<br>(6)"OPENMP=1" to build with OpenMP support to accelerate Yolo by using multi-core CPU</br>
<br>(7)"LIBSO=1" to build a library `darknet.so` and binary runable file `uselib` that uses this library. <br>Or you can try to run so `LD_LIBRARY_PATH=./:$LD_LIBRARY_PATH ./uselib test.mp4` How to use this SO-library from your own code - you can look at C++ example: https://github.com/AlexeyAB/darknet/blob/master/src/yolo_console_dll.cpp
    or use in such a way: `LD_LIBRARY_PATH=./:$LD_LIBRARY_PATH ./uselib data/coco.names cfg/yolov3.cfg yolov3.weights test.mp4`</br>
<br><b> 3.Download the pretrain weights for YOLOv3 from https://pjreddie.com/media/files/darknet53.conv.74</b></br>
<br><b> 4.create yolov3_obj.cfg same content as yolov3.cfg and modify some place as following</b></br>
<br>There are three places with classes in the cfg,change it to your classes</br>
<br>There are three places with filters in the cfg,change the number by "(classes + 5)x3)"</br>
<br>offical recommend to set cfg file(head) batch=64 and subdivisions=8, my setting in FinalWeights file</br>
<br></br>
<br><b> 5.Create file obj.names in the directory build\darknet\x64\data\, with objects names - each in new line</b></br>
<br><b> 6.Create file obj.data in the directory build\darknet\x64\data\, containing (where classes = number of objects):</b></br>
<br>classes= 2</br>
<br>train  = data/train.txt</br>
<br>valid  = data/test.txt</br>
<br>names = data/obj.names</br>
<br>backup = backup/</br>
<br><b> 7.Follow the "COCO2YOLO" folder to transform your data format into YOLO(txt) and picture</b></br>
<br><b> 8.Put image-files and YOLO file of your objects in the directory build\darknet\x64\data\obj\</b></br>
<br> the format of YOLO is <object-class> <x> <y> <width> <height></br>
<br> <object-class> is following your name file,from 0 to n</br>
<br><b> 9.</b></br>
<br><b> 10.</b></br>
<br><b> 11.</b></br>
<br><b> 12.</b></br>
