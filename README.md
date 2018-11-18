# Convert2Yolo
Object Detection annotation Convert to [Yolo Darknet](https://pjreddie.com/darknet/yolo/) Format

Support DataSet : 

1. COCO
2. VOC
3. UDACITY Object Detection
4. KITTI 2D Object Detection

​    

### Pre-Requiredment

```
pip3 install -r requirements.txt
```

​    

### Required Parameters 

each dataset requried some parameters

see example.py

    1. Dataset Category
       - like a COCO / VOC / UDACITY / KITTI
    2. Image path
       - it directory path. not file path
    3. annotation path
       - it directory path. not file path
    4. output path
       - it directory path. not file path
    5. image type
       - like a `*.png`, `*.jpg`
    6. manipast file path
       - it need train yolo model in [darknet framework](https://pjreddie.com/darknet/)
    7. class list file path(*.names)
       - it is `*.txt` file contain class name. reference [darknet `*.name` file](https://github.com/pjreddie/darknet/blob/master/data/voc.names)

​    

### *.names file example
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

### 1. example Code
```bash
python3 example.py --datasets [COCO/VOC/KITTI/UDACITY] --img_path <image_path> --label <label path or annotation file> --convert_output_path <output path> --img_type [".jpg" / ".png"] --manipast_path <output manipast file path> --cls_list_file <*.names file path>

>>
ex) python3 example.py --datasets KITTI --img_path ./example/kitti/images/ --label ./example/kitti/labels/ --convert_output_path ./ --img_type ".jpg" --manipast_path ./ --cls_list_file names.txt
```

​    

### TODO

- [x] Support VOC Pascal Format
- [x] Support Udacity Format
- [x] Support COCO Format
- [x] Support KITTI Format
- [x] Write README
- [x] Code Refactoring
