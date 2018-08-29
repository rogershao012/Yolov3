# Yolov3
Yolov3 instruction for handover
original project from 
https://github.com/AlexeyAB/darknet

<h3>Following is some introductions and files base on the repository:</h3>
<ul>
<li><b>Finalweights Folder</b> -> <b>Introduce of my training setting and weights file</b></li>
<li><b>COCO2YOLO Folder</b> -> <b>Change COCO format to YOLO format and provide tool to show file path</b></li>
<li><b>changeFile Folder</b> -> <b>files which easy to output coco format</b></li>
<li><b>TransformJson Folder</b> -> <b>Transform output result to json format</b></li> 
<li><b>tackleHabcam Folder</b> -> <b>Tackle with no annotation and divide picture of Habcam</b></li> 
</ul>

<h3>STEPS:</h3>
<br><b> 1.Download the original project from https://github.com/AlexeyAB/darknet and check the Requires </b></br>
<br><b> 2.Go to its dictionary and open Makefile to change as following and do make in the directory</b>
<ul>
<li>(1)"GPU=1" to build with CUDA to accelerate by using GPU (CUDA should be in `/usr/local/cuda`)</li>
<li>(2)"CUDNN=1" to build with cuDNN v5-v7 to accelerate training by using GPU (cuDNN should be in `/usr/local/cudnn`)</li>
<li>(3)"CUDNN_HALF=1" to build for Tensor Cores (on Titan V / Tesla V100 / DGX-2 and later) speedup Detection 3x, Training 2x</li>
<li>(4)"OPENCV=1" to build with OpenCV 3.x/2.4.x - allows to detect on video files and video streams from network cameras or web-cams</li>
<li>(5)"DEBUG=1" to bould debug version of Yolo</li>
<li>(6)"OPENMP=1" to build with OpenMP support to accelerate Yolo by using multi-core CPU</li>
<li>(7)"LIBSO=1" to build a library `darknet.so` and binary runable file `uselib` that uses this library. </li>
    <li>Or you can try to run so `LD_LIBRARY_PATH=./:$LD_LIBRARY_PATH ./uselib test.mp4` How to use this SO-library from your own code - you can look at C++ example: https://github.com/AlexeyAB/darknet/blob/master/src/yolo_console_dll.cpp
    or use in such a way: `LD_LIBRARY_PATH=./:$LD_LIBRARY_PATH ./uselib data/coco.names cfg/yolov3.cfg yolov3.weights test.mp4`</br>
    </li></ul>
    
<br><b> 3.Download the pretrain weights for YOLOv3 from https://pjreddie.com/media/files/darknet53.conv.74 and put to the directory build\darknet\x64</b></br>
<br><b> 4.create yolov3_obj.cfg same content as yolov3.cfg and modify some place as following</b>
<ul>
<li>There are three places with classes in the cfg,change it to your classes</li>
<li>There are three places with filters in the cfg,change the number by "(classes + 5)x3)"</li>
<li>offical recommend to set cfg file(head) batch=64 and subdivisions=8, my setting in FinalWeights folder</li>
</ul>
<br><b> 5.Create file obj.names in the directory build\darknet\x64\data\, with objects names - each in new line</b></br>
<br><b> 6.Create file obj.data in the directory build\darknet\x64\data\, containing (where classes = number of objects):</b>
<ul>
<li>classes= 2</li>
<li>train  = data/train.txt</li>
<li>valid  = data/test.txt</li>
<li>names = data/obj.names</li>
<li>backup = backup/</li>
</ul>
<br><b> 7.Follow the "COCO2YOLO" folder to transform your data format into YOLO(txt) and picture</b></br>
<br><b> 8.Put image-files and YOLO file of your objects in the directory build\darknet\x64\data\obj\</b>
<ul>
<li> the format of YOLO is (object-class) (x) (y) (width) (height)</li>
<li> "(object-class)" is following your name file,from 0 to n</li>
<li> Remember to divide you pic path into train,valid,or (test)</li>
</ul>

<h5> * If you want to modify habcam dataset,there is something can us in tackleHabcam folder</h5>

<br><b> 9.If you want to modify anchor size,cmd "./darknet detector calc_anchors data/obj.data -num_of_clusters 9 -width 416 -height 416" and it will show up on terminal and anchor.txt,then replace it to cfg file anchor </b></br>
<br><b> 10.If you want to process CLAHE,just use the CLAHE folder's python file.</b></br>
<ul>
    <li>Remember picture still have to stay with YOLO(txt) to train</li>
</ul>

<br><b> 11.Start training by using the command line: ./darknet detector train data/obj.data yolo-obj.cfg darknet53.conv.74</b>
<ul>
<li>file yolo-obj_xxx.weights will be saved to the build\darknet\x64\backup\ for each 100 iterations</li>
<li>To disable Loss-Window use darknet.exe detector train data/obj.data yolo-obj.cfg darknet53.conv.74 -dont_show, if you train on computer without monitor like a cloud Amazaon EC2</li>
<li>If you want to submit the COCO format,Change two files in src with changeFile folder's file</li>
</ul>
<br><b> 12.After training is complete - get result yolo-obj_final.weights from path build\darknet\x64\backup\</b>
<ul>
<li> After each 100 iterations you can stop and later start training from this point and just change darknet53.conv.74 to the new file</li>
<li> If during training you see nan values for avg (loss) field - then training goes wrong, but if nan is in some other lines - then training goes well.</li>
<li> If you changed width= or height= in your cfg-file, then new width and height must be divisible by 32.</li>
<li> After training use such command for detection: ./darknet detector test data/obj.data yolo-obj.cfg yolo-obj_8000.weights</li>
<li> if error Out of memory occurs then in .cfg-file you should increase subdivisions=16, 32 or 64(or decrease the batch size)</li>
</ul>
<br><b> 13.if you want to check map ./darknet detector map data/obj.data yolo-obj.cfg yolo-obj_8000.weights</b></br>
<br><b> 14.if you want to test map, just change the obj.data's valid path and execute step 11 to test file</b></br>
<br><b> 15.if you want to output,just run "./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights -dont_show -ext_output <<train.txt>train.txt> result.txt </b></br>
<ul>
    <li>train.txt is the image path file</li>
    <li>result.txt is the file you output</li>
    <li>train.txt can get from add2name.py no matter you want to train or test</li>
</ul>
<br><b> 16.Use transformJson Folder file to convert Step 14 output to Json format </b></br>
