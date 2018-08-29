<h1>The Folder is introduce of the training setting of my task</h1>

Because the weights file is too large,So I upload it to:
<br>https://drive.google.com/drive/folders/1Ls6gTASiK5ynh4mEuVKJFciQFtymRVoa?usp=sharing</br>

<h4>Following is some information about setting of cfg file <for each dataset(special part):</h4>

<h3>mbari</h3>
<ul>
<li>batch=8</li>
<li>subdivisions=2</li>
<li>width=416</li>
<li>height=416</li>
<li>learning_rate=0.0005</li>
<li>max_batches=75000</li>
<li>steps=30000,50000</li>
<li>scales=.2,.2</li>
</ul>

<h3>habcam</h3>
<ul>
<li>batch=16</li>
<li>subdivisions=4</li>
<li>width=416</li>
<li>height=416</li>
<li>learning_rate=0.0005</li>
<li>max_batches=200000</li>
<li>steps=120000,150000,195000</li>
<li>scales=.5,.2,.1</li>
</ul>

<h3>mouss0</h3>
<ul>
<li>batch=16</li>
<li>subdivisions=4</li>
<li>width=416</li>
<li>height=416</li>
<li>learning_rate=0.001</li>
<li>max_batches=40000</li>
<li>steps=400000,450000</li>
<li>scales=.2,.2</li>
</ul>

<h3>mouss1</h3>
<ul>
<li>batch=16</li>
<li>subdivisions=4</li>
<li>width=416</li>
<li>height=416</li>
<li>learning_rate=0.0005</li>
<li>max_batches=50000</li>
<li>steps=40000,450000</li>
<li>scales=.2,.2</li>
</ul>
