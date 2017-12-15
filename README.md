# Convert2Yolo
Object Detection & Recognition DataSet annotation Convert [Yolo Darknet](https://pjreddie.com/darknet/yolo/)

### Pre-Requiredment
#### 1. Make Directory
All convert code need some directory hierarchy

just make folder like this

```

[some your project root directory]
|
| - [JPEG] : For images folder
|
| - [label] : For annotaion folder
|
| - [results] : For results of convert2Yolo

```

#### 2. Make Classe file
you should make class file

follow this format

reference voc.names file in repository

##### voc.names
```
aeroplane
bicycle
bird
boat
bottle
bus
car
cat
chair
cow
diningtable
dog
horse
motorbike
person
pottedplant
sheep
sofa
train
tvmonitor
```

#### 3. Install requirement package
```
pip3 install -r pip_install_required.txt
```

### VOC Pascal Format
Here is VOC Pascal DataSet example

![voc image](image/voc_image.png)
![voc xml](image/voc_xml.png)

#### 1. example Code
```
python voc.py test.names example/voc/JPEG/ example/voc/label/ example/voc/results/
```

### TODO
- [x] Support VOC Pascal Format
- [x] Support Udacity Format
- [x] Write how to using VOC Pascal Format in ReadMe
- [ ] Write how to using Udacity Format in ReadMe
- [ ] Code Refactoring