<h3>This folder contains python files to convert COCO format to Yolo format</h3>

<h4>Order in sequence : transform.py -> makexml.py -> xml2txt.py -> pic2txt.py </h4>
<ul>
<li><h4>transform.py</h4></li>
<ul>
  <li><b>Remember:</b> modify name, number and json file</li>
  <li><b>Purpose :</b> Read json file and transform into unified format of json</li>
</ul>
<li><h4>makexml.py</h4></li>
<ul>
  <li><b>Remember</b>: modify image size(if different with original),image path</li>
  <li><b>Purpose </b>: make json file into individual json file</li>
</ul>
<li><h4>xml2txt.py</h4></li>
<ul>
  <li><b>Remember</b>: modify the pic with png or jpg,change the index names(if you delete,sometimes if fail?)</li>
  <li><b>Purpose </b>: make the picture with its yolo format document</li>
  <li><b>Usage </b>: python xml2txt.py 0 [source folder name] [deststion folder name] [voc name file]</li>
  <li><b>Usage explain </b>:source folder name(Where you put xml with pic),deststion folder name(where you put txt(yolo) with pic),voc name file(the name ) </li>
</ul>
<li><h4>pic2txt.py</h4></li>
<ul>
  <li><b>Remember</b>: </li>
  <li><b>Purpose </b>: </li>
</ul>
