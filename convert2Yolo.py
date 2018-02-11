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
import csv
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse

class color:
    BOLD = '\033[1m'
    END = '\033[0m'
    DEFAULT = '\033[0;37;40m'
    RED = '\033[91m'

class convert2Yolo(object):

    def __init__(self, classes_path, image_type="jpg", image_dir = "example/voc/JPEG/", anno_dir = "example/voc/label/", label_dir = "example/voc/results/", manifest_dir="example/voc/"):

        self.classes = self.read_class(classes_path)
        self.image_dir = image_dir
        self.anno_dir = anno_dir
        self.output_dir = label_dir
        self.image_type = "." + image_type
        self.manifest_dir = manifest_dir

    def convertCoordinate(self,size, box):
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

    def read_class(self,path):
        with open(path, 'r') as file:
            l = file.read().splitlines()
        return l

    def indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def Udacity2Voc(self, dataSet_dir = "example/udacity/", anno_dir = "label/labels.csv", label_dir = "results/", label_list = None):
        print(color.BOLD + color.RED + "------------------------- CSV Parsing Start-------------------------" + color.END)

        if label_list is None:
            label_list = self.label_list

        work_dir = getcwd() + "/" + dataSet_dir
        anno_dir = work_dir + anno_dir
        label_dir = work_dir + label_dir

        print("Input file : {}".format(anno_dir))

        f = open(anno_dir, 'r', encoding='utf-8')
        l = csv.reader(f)
        try:
            for line in l:
                print(color.BOLD + color.RED + "------------------------- CSV Parsing -------------------------" + color.END)
                convertList = line[0].split(" ")
                length = len(convertList)

                image_name = convertList[0]
                xmin = convertList[1]
                ymin = convertList[2]
                xmax = convertList[3]
                ymax = convertList[4]
                label = convertList[6].split('"')[1]

                if length is 8:
                    state = convertList[7].split('"')[1]
                    label = label + state

                # Open output result files

                img = Image.open(dataSet_dir + "JPEG/" + image_name)
                img_width = int(img.size[0])
                img_height = int(img.size[1])
                img_depth = 3 #int(img.size[2])

                print("image size (width, height) : {}".format(img.size))
                print()

                print("Output : {}".format(label_dir + image_name[:-3] + "xml"))
                print()

                print("class name, index : ({})".format(label))

                result_outpath = str(label_dir + image_name[:-3] + "xml")

                if not os.path.isfile(result_outpath):
                    xml_annotation = Element("annotation")

                    xml_folder = Element("folder")
                    xml_folder.text = "udacity"

                    xml_annotation.append(xml_folder)

                    xml_filename = Element("filename")
                    xml_filename.text = str(image_name)
                    xml_annotation.append(xml_filename)

                    xml_path = Element("path")
                    xml_path.text = str(label_dir + image_name)
                    xml_annotation.append(xml_path)

                    xml_source = Element("source")

                    xml_database = Element("database")
                    xml_database.text = "Unknown"
                    xml_source.append(xml_database)
                    xml_annotation.append(xml_source)

                    xml_size = Element("size")
                    xml_width = Element("width")
                    xml_width.text = str(img_width)
                    xml_size.append(xml_width)

                    xml_height = Element("height")
                    xml_height.text = str(img_height)
                    xml_size.append(xml_height)

                    xml_depth = Element("depth")
                    xml_depth.text = str(img_depth)
                    xml_size.append(xml_depth)

                    xml_annotation.append(xml_size)

                    xml_segmented = Element("segmented")
                    xml_segmented.text = "0"

                    xml_annotation.append(xml_segmented)

                    xml_object = Element("object")

                    xml_name = Element("name")
                    xml_name.text = label
                    xml_object.append(xml_name)

                    xml_pose = Element("pose")
                    xml_pose.text = "Unspecified"
                    xml_object.append(xml_pose)

                    xml_truncated = Element("truncated")
                    xml_truncated.text = "0"
                    xml_object.append(xml_truncated)

                    xml_difficult = Element("difficult")
                    xml_difficult.text = "0"
                    xml_object.append(xml_difficult)

                    xml_bndbox = Element("bndbox")
                    xml_xmin = Element("xmin")
                    xml_xmin.text = str(xmin)
                    xml_bndbox.append(xml_xmin)

                    xml_ymin = Element("ymin")
                    xml_ymin.text = str(ymin)
                    xml_bndbox.append(xml_ymin)

                    xml_xmax = Element("xmax")
                    xml_xmax.text = str(xmax)
                    xml_bndbox.append(xml_xmax)

                    xml_ymax = Element("ymax")
                    xml_ymax.text = str(ymax)
                    xml_bndbox.append(xml_ymax)
                    xml_object.append(xml_bndbox)

                    xml_annotation.append(xml_object)

                    self.indent(xml_annotation)
                    dump(xml_annotation)
                    ElementTree(xml_annotation).write(result_outpath)
                else:
                    tree = parse(result_outpath)
                    xml_annotation = tree.getroot()
                    xml_object = Element("object")

                    xml_name = Element("name")
                    xml_name.text = label
                    xml_object.append(xml_name)

                    xml_pose = Element("pose")
                    xml_pose.text = "Unspecified"
                    xml_object.append(xml_pose)

                    xml_truncated = Element("truncated")
                    xml_truncated.text = "0"
                    xml_object.append(xml_truncated)

                    xml_difficult = Element("difficult")
                    xml_difficult.text = "0"
                    xml_object.append(xml_difficult)

                    xml_bndbox = Element("bndbox")
                    xml_xmin = Element("xmin")
                    xml_xmin.text = str(xmin)
                    xml_bndbox.append(xml_xmin)

                    xml_ymin = Element("ymin")
                    xml_ymin.text = str(ymin)
                    xml_bndbox.append(xml_ymin)

                    xml_xmax = Element("xmax")
                    xml_xmax.text = str(xmax)
                    xml_bndbox.append(xml_xmax)

                    xml_ymax = Element("ymax")
                    xml_ymax.text = str(ymax)
                    xml_bndbox.append(xml_ymax)
                    xml_object.append(xml_bndbox)

                    xml_annotation.append(xml_object)
                    self.indent(xml_annotation)
                    dump(xml_annotation)
                    ElementTree(xml_annotation).write(result_outpath)


                print(color.BOLD + color.RED + "------------------------- CSV Parsing -------------------------" + color.END)



            print(color.BOLD + color.RED + "------------------------- CSV Parsing END -------------------------" + color.END)
        except Exception as e:
            print(color.BOLD + color.RED + "ERROR : {}".format(e) + color.END)


################################################################################################################

    def parsingUdacity(self, dataSet_dir = "example/udacity/", anno_dir = "label/labels.csv", label_dir = "results/", label_list = None):
        print(color.BOLD + color.RED + "------------------------- CSV Parsing Start-------------------------" + color.END)

        if label_list is None:
            label_list = self.label_list

        work_dir = getcwd() + "/" + dataSet_dir
        anno_dir = work_dir+anno_dir
        label_dir = work_dir + label_dir

        list_file = open('%s/%s_list.txt' % (work_dir, label_list), 'w')
        print("Input file : {}".format(anno_dir))


        f = open(anno_dir, 'r', encoding='utf-8')
        l = csv.reader(f)
        try:
            for line in l:
                print(
                    color.BOLD + color.RED + "------------------------- CSV Parsing -------------------------" + color.END)
                convertList = line[0].split(" ")
                length = len(convertList)

                image_name = convertList[0]
                xmin = convertList[1]
                ymin = convertList[2]
                xmax = convertList[3]
                ymax = convertList[4]
                label = convertList[6].split('"')[1]

                if length is 8:
                    state = convertList[7].split('"')[1]
                    label = label + state

                # Open output result files
                result_outpath = str(label_dir + image_name[:-3] + "txt")
                if not os.path.isfile(result_outpath):
                    result_outfile = open(result_outpath, "w")
                else:
                    result_outfile = open(result_outpath, "a")

                img = Image.open(dataSet_dir + "JPEG/" + image_name)
                img_width = int(img.size[0])
                img_height = int(img.size[1])

                print("image size (width, height) : {}".format(img.size))
                print()
                print("Output : {}".format(label_dir + image_name[:-3] + "txt"))
                print()

                b = [float(xmin), float(xmax), float(ymin), float(ymax)]
                bb = self.convertCoordinate((img_width, img_height), b)

                cls_id = self.classes.index(label)

                print("class name, index : ({},{})".format(label, cls_id))
                print("bndbox Size : ({})".format(b))
                print("convert result : ({})".format(bb))
                result_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
                list_file.writelines('%s%s.jpg\n' % (work_dir, os.path.splitext(image_name)[0]))
                print(
                    color.BOLD + color.RED + "------------------------- CSV Parsing -------------------------" + color.END)
            list_file.close()
            print(
                color.BOLD + color.RED + "------------------------- CSV Parsing END -------------------------" + color.END)
        except Exception as e:
            print(color.BOLD + color.RED + "ERROR : {}".format(e) + color.END)

    def parsingVocXML(self, image_dir=None, anno_dir=None, label_dir=None, label_list=None):

        if image_dir is None:
            image_dir = self.image_dir
        if anno_dir is None:
            anno_dir = self.anno_dir
        if label_dir is None:
            label_dir = self.label_dir
        if label_list is None:
            label_list = self.label_list

        work_dir = getcwd()
        list_file = list_file = open('%s/%s_list.txt' % (work_dir, label_list), 'w')

        # Get input text file list
        xml_list = []

        for (dirpath, dirnames, filenames) in walk(anno_dir):
            xml_list.extend(filenames)

        print(color.BOLD + color.RED + "------------------------- XML File LIST -------------------------" + color.END)
        print(color.BOLD + "xml file list : {}".format(xml_list) + color.END)
        print(color.BOLD + color.RED + "------------------------- XML File LIST -------------------------" + color.END)

        try:

            # Process
            for xml_name in xml_list:
                print(color.BOLD + color.RED +"------------------------- XML Parsing -------------------------" + color.END)

                # open xml file
                xml_path = anno_dir + xml_name
                xml_file = open(xml_path, "r")

                print("Input file : {}".format(xml_path))

                tree = ET.parse(xml_file)
                root = tree.getroot()

                size = root.find('size')
                if size == None:
                    raise Exception("cannot find size tag, size tag is basic information!")

                xml_width = int(size.find('width').text)
                xml_height = int(size.find('height').text)

                img_path = str('%s/%s.jpg' % (image_dir, os.path.splitext(xml_name)[0]))

                objects = root.findall('object')
                if len(objects) == 0:
                    print(color.BOLD + color.RED + "ERROR : can't find object tag" + color.END)


                    if os.path.exists(xml_path):
                        xml_file.close()
                        os.remove(xml_path)
                    if os.path.exists(img_path):
                        xml_file.close()
                        os.remove(img_path)

                    continue

                # open Image file
                img = Image.open(img_path)
                img_width = int(img.size[0])
                img_height = int(img.size[1])

                print('Image path : ' + img_path + '\n')
                print("xml size (width, height) : " + "(" + str(xml_width) + ',' + str(xml_height) + ")")
                print('image size (width, height) : ' + "(" + str(img_width) + ',' + str(img_height) + ")\n")

                if not xml_width == img_width or not xml_height == img_height:
                    print(color.BOLD + color.RED + "xml and image size different" + color.END)
                    raise Exception("xml and image size different")

                # Open output result files
                result_outpath = str(self.root_dir + label_dir + xml_name[:-3] + "txt")
                result_outfile = open(result_outpath, "w")
                print("Output:" + result_outpath + '\n')

                for object in objects:

                    cls = object.find('name').text
                    if cls == None:
                        raise Exception("can't find name tag")
                    elif cls not in self.classes:
                        raise Exception("name tag not involve this classes")

                    bndbox = object.find('bndbox')
                    if bndbox == None:
                        if os.path.exists(xml_path):
                            xml_file.close()
                            os.remove(xml_path)
                        if os.path.exists(img_path):
                            xml_file.close()
                            os.remove(img_path)
                        raise Exception("can't find bndbox tag")

                    xmin = int(bndbox.find('xmin').text)
                    xmax = int(bndbox.find('xmax').text)
                    ymin = int(bndbox.find('ymin').text)
                    ymax = int(bndbox.find('ymax').text)

                    b = (float(xmin), float(xmax), float(ymin), float(ymax))
                    bb = self.convertCoordinate((img_width, img_height), b)

                    cls_id = self.classes.index(cls)
                    print('class name, index : ' + '(' + str(cls) + ", " + str(cls_id) + ')')
                    print("bndbox Size : " + str(b))
                    print("convert result : " + str(bb) + '\n')
                    result_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

                result_outfile.close()
                list_file.writelines('%s%s.jpg\n' % (self.root_dir + image_dir, os.path.splitext(xml_name)[0]))

            list_file.close()
            print(color.BOLD + color.RED +"------------------------- XML Parsing -------------------------" + color.END)

        except Exception as e:
            print(color.BOLD + color.RED + "ERROR : {}".format(e) + color.END)

            if not result_outfile.closed:
                print(color.BOLD + color.RED + "Close result_outfile" + color.END)
                result_outfile.close()
            if os.path.exists(result_outpath):
                print(color.BOLD + color.RED + "delete result outpath" + color.END)
                os.remove(result_outfile)