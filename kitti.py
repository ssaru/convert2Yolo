# -*- coding: utf-8 -*-

"""
Created on Mon Mar  13 15:40:43 2016
This script is to convert the txt annotation files to appropriate format needed by YOLO
@author: Martin Hwang
Email: dhhwang89@gmail.com
"""

import os
from os import walk, getcwd
from PIL import Image
import xml.etree.ElementTree as ET
import math

class color:
    BOLD = '\033[1m'
    END = '\033[0m'
    DEFAULT = '\033[0;37;40m'
    RED = '\033[91m'

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (round(x,3), round(y,3), round(w,3), round(h,3))

# Custom define class
classes = ["Skier", "Skigate", "Person", "Billboard"]

# Configure Paths
annotation_path = "/media/martin/My Passport/datasets/kitti/label/"
yolo_label_path = "/media/martin/My Passport/datasets/z_darknet/"
image_path = "/media/martin/My Passport/datasets/kitti/JPEG/"


list_file_name = "ski"

wd = getcwd()
list_file = open('%s/%s_list.txt' % (wd, list_file_name), 'w')

# Get input text file list
txt_name_list = []

'''
example = "example/kitti/000021.txt"
txt_file = open(example, "r")
l = []
for data in txt_file:
    l.append(data)
'''
for (dirpath, dirnames, filenames) in walk(annotation_path):
    txt_name_list.extend(filenames)
    break

print(color.BOLD + "txt file list : {}".format(txt_name_list) + color.END + '\n')

try:

    #Process
    for txt_name in txt_name_list:
        print('------------------------------------------------------------------------')
        # open txt file
        txt_path = annotation_path + txt_name
        txt_file = open(txt_path, "r")

        print("Input file : " + txt_path)

        img_path = image_path + txt_name[0:-4] + ".jpg"
        print("Image file : {}".format(img_path))
        img = Image.open(img_path)

        img_width = int(img.size[0])
        img_height = int(img.size[1])

        print("Image width : {}, height : {}".format(img_width, img_height))

        result_outpath = str(yolo_label_path + txt_name[:-3] + "txt")
        result_outfile = open(result_outpath, "w")
        print("Output:" + result_outpath + '\n')

        for data in txt_file:
            split = data.split(" ")

            label = split[0]
            xmin = int(split[4])
            ymin = int(split[5])
            xmax = int(split[6])
            ymax = int(split[7])

            print('origin : {}'.format(split))
            print("xmin : {}, ymin : {}, xmax : {}, ymax : {}".format(xmin, ymin, xmax, ymax))

            cls = label
            if cls == None:
                raise Exception("can't find name tag")
            elif cls not in classes:
                raise Exception("name tag not involve this classes")

            b = (float(xmin), float(xmax), float(ymin), float(ymax))
            bb = convert((img_width, img_height), b)

            cls_id = classes.index(cls)

            print('class name, index : ' + '(' + str(cls) + ", " + str(cls_id) + ')')
            print("bndbox Size : " + str(b))
            print("convert result : " + str(bb) + '\n')
            result_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

        result_outfile.close()
        list_file.writelines('%s%s.jpg\n' % ( image_path,os.path.splitext(txt_name)[0]))


    list_file.close()



except Exception as e:

    print(color.BOLD + color.RED + "ERROR : {}".format(e) + color.END)

    if not result_outfile.closed:
        print(color.BOLD + color.RED + "Close result_outfile" + color.END)
        result_outfile.close()
    if os.path.exists(result_outpath):
        print(color.BOLD + color.RED + "delete result outpath" + color.END)
        os.remove(result_outfile)

