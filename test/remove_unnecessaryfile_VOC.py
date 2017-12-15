# -*- coding: utf-8 -*-
import os
from os import walk, getcwd
from PIL import Image
import xml.etree.ElementTree as ET
from shutil import copyfile

# Configure Paths
img_path = "/media/martin/enumcut/EnumNet/EnumCut/DataSet/VOC/person_v1/person/jpeg/"
label_path = "/media/martin/enumcut/EnumNet/EnumCut/DataSet/VOC/person_v1/person/labels/"
save_path = "/media/martin/enumcut/EnumNet/EnumCut/DataSet/VOC/person_v1/person/complete/"

annotation_path = "/media/martin/enumcut/EnumNet/EnumCut/DataSet/VOC/person_v1/person/Annotations/"

img_list = []
label_list = []

label_filename = []
img_filename = []
for (dirpath, dirnames, filenames) in walk(label_path):
    label_list.extend(filenames)
    break

for (dirpath, dirnames, filenames) in walk(img_path):
    img_list.extend(filenames)
    break


for name in label_list:
    label_filename.append(name[0:-4])

for name in img_list:
    img_filename.append(name[0:-4])


for label in label_filename:
    for img in img_filename:
        if label == img:
            copyfile(img_path+img+".jpg", save_path+"JPEG/"+img+".jpg")
            copyfile(annotation_path+label+".xml", save_path+"label/"+label+".xml")



