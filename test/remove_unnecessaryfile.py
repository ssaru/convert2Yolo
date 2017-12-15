# -*- coding: utf-8 -*-
import os
from os import walk, getcwd
from PIL import Image
import xml.etree.ElementTree as ET
from shutil import copyfile

# Configure Paths
#'/media/martin/enumcut/EnumNet/EnumCut/DataSet/Instagram/basketball/1.0'
img_path = "/home/martin/Desktop/_1. finished/JPEG/"
label_path = "/home/martin/Desktop/_1. finished/labels/"
save_path = "/home/martin/Desktop/_2. complete/"

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

print(img_list)
print(label_list)


for name in label_list:
    label_filename.append(name[0:-4])

for name in img_list:
    img_filename.append(name[0:-4])


for label in label_filename:
    for img in img_filename:
        if label == img:
            copyfile(img_path+img+".png", save_path+"JPEG/"+img+".jpg")
            copyfile(label_path+label+".xml", save_path+"label/"+label+".xml")



