# Convert2Yolo
Object Detection annotation Convert to [Yolo Darknet](https://pjreddie.com/darknet/yolo/) Format

Support DataSet : 

1. COCO
2. VOC
3. UDACITY Object Detection
4. KITTI 2D Object Detection

### Pre-Requiredment

```
pip3 install -r requirements.txt
```

### Required Parameters 

each dataset requried some parameters

see example.py

  1. Dataset Category
  2. Image path
  3. annotation path
  4. output path
  5. image type
  6. manipast file path
  7. class list file path(*.names)
  
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
```
python3 example.py --datasets [COCO/VOC/KITTI/UDACITY] --image_path <image_path> --label <label path or annotation file> --convert_output_path <output path> --image_type [".jpg" / ".png"] --manipast_path <output manipast file path> --clas_list_file <*.names file path>
```

### TODO
- [x] Support VOC Pascal Format
- [x] Support Udacity Format
- [x] Support COCO Format
- [x] Support KITTI Format
- [x] Write README
- [x] Code Refactoring