import sys
import os

import xml.etree.ElementTree as Et
from xml.etree.ElementTree import Element, ElementTree

import json

from xml.etree.ElementTree import dump

# Common Data format
"""
{
    "filename" :      
                {                  
                    "size" :
                                {
                                    "width" : <string>
                                    "height" : <string>
                                    "depth" : <string>
                                }
                
                    "objects" :
                                {
                                    "num_obj" : <int>
                                    "<index>" :
                                                {
                                                    "name" : <string>
                                                    "bndbox" :
                                                                {
                                                                    "xmin" : <string>
                                                                    "ymin" : <string>
                                                                    "xmax" : <string>
                                                                    "ymax" : <string>
                                                                }
                                                }
                                    ...
                
                
                                }
                }
"""

# XML Data format
"""
{
    "filename" : <XML Object>
    ...
}
"""


class VocPascal:
    """
    Handler Class for VOC PASCAL Format
    """

    def xml_indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.xml_indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def generate(self, data):
        try:

            xml_list = {}
            for key in data:
                element = data[key]

                xml_annotation = Element("annotation")

                xml_size = Element("size")
                xml_width = Element("width")
                xml_width.text = element["size"]["width"]
                xml_size.append(xml_width)

                xml_height = Element("height")
                xml_height.text = element["size"]["height"]
                xml_size.append(xml_height)

                xml_depth = Element("depth")
                xml_depth.text = element["size"]["depth"]
                xml_size.append(xml_depth)

                xml_annotation.append(xml_size)

                xml_segmented = Element("segmented")
                xml_segmented.text = "0"

                xml_annotation.append(xml_segmented)

                if int(element["objects"]["num_obj"]) < 1:
                    return False, "number of Object less than 1"

                for i in range(0, int(element["objects"]["num_obj"])):

                    xml_object = Element("object")
                    obj_name = Element("name")
                    obj_name.text = element["objects"][str(i)]["name"]
                    xml_object.append(obj_name)

                    obj_pose = Element("pose")
                    obj_pose.text = "Unspecified"
                    xml_object.append(obj_pose)

                    obj_truncated = Element("truncated")
                    obj_truncated.text = "0"
                    xml_object.append(obj_truncated)

                    obj_difficult = Element("difficult")
                    obj_difficult.text = "0"
                    xml_object.append(obj_difficult)

                    xml_bndbox = Element("bndbox")

                    obj_xmin = Element("xmin")
                    obj_xmin.text = element["objects"][str(i)]["bndbox"]["xmin"]
                    xml_bndbox.append(obj_xmin)

                    obj_ymin = Element("ymin")
                    obj_ymin.text = element["objects"][str(i)]["bndbox"]["ymin"]
                    xml_bndbox.append(obj_ymin)

                    obj_xmax = Element("xmax")
                    obj_xmax.text = element["objects"][str(i)]["bndbox"]["xmax"]
                    xml_bndbox.append(obj_xmax)

                    obj_ymax = Element("ymax")
                    obj_ymax.text = element["objects"][str(i)]["bndbox"]["ymax"]
                    xml_bndbox.append(obj_ymax)
                    xml_object.append(xml_bndbox)

                    xml_annotation.append(xml_object)

                self.xml_indent(xml_annotation)

                xml_list[key.split(".")[0]] = xml_annotation

            return True, xml_list

        except Exception as e:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            msg = "ERROR : {}, moreInfo : {}\t{}\t{}".format(e, exc_type, fname, exc_tb.tb_lineno)

            return False, msg

    @staticmethod
    def save(xml_list, path):

        try:
            path = os.path.abspath(path)
            for key in xml_list:
                xml = xml_list[key]
                filepath = os.path.join(path, "".join([key, ".xml"]))
                ElementTree(xml).write(filepath)

            return True, None

        except Exception as e:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            msg = "ERROR : {}, moreInfo : {}\t{}\t{}".format(e, exc_type, fname, exc_tb.tb_lineno)

            return False, msg

    @staticmethod
    def parse(path):
        try:

            (dir_path, dir_names, filenames) = next(os.walk(os.path.abspath(path)))
            print([dir_path, dir_names, filenames])

            data = {}
            for filename in filenames:

                xml = open(os.path.join(dir_path, filename), "r")
    
                tree = Et.parse(xml)
                root = tree.getroot()

                xml_size = root.find("size")
                size = {
                    "width": xml_size.find("width").text,
                    "height": xml_size.find("height").text,
                    "depth": xml_size.find("depth").text

                }

                objects = root.findall("object")
                if len(objects) == 0:
                    return False, "number object zero"

                obj = {
                    "num_obj": len(objects)
                }
    
                obj_index = 0
                for _object in objects:

                    tmp = {
                        "name": _object.find("name").text
                    }

                    xml_bndbox = _object.find("bndbox")
                    bndbox = {
                        "xmin": xml_bndbox.find("xmin").text,
                        "ymin": xml_bndbox.find("ymin").text,
                        "xmax": xml_bndbox.find("xmax").text,
                        "ymax": xml_bndbox.find("ymax").text
                    }
                    tmp["bndbox"] = bndbox
                    obj[str(obj_index)] = tmp

                    obj_index += 1

                annotation = {
                    "size": size,
                    "objects": obj
                }

                data[root.find("filename").text.split(".")[0]] = annotation

            return True, data

        except Exception as e:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            msg = "ERROR : {}, moreInfo : {}\t{}\t{}".format(e, exc_type, fname, exc_tb.tb_lineno)

            return False, msg


class Coco:
    """
    Handler Class for VOC PASCAL Format
    """

    @staticmethod
    def parse(json_path):

        json_data = json.load(open(json_path))

        images_info = json_data["images"]
        cls_info = json_data["categories"]


        data = {}

        cnt = 0

        for anno in json_data["annotations"]:

            image_id = anno["image_id"]
            cls_id = anno["category_id"]

            filename = None
            img_width = None
            img_height = None

            for info in images_info:
                    if info["id"] == image_id:
                        filename, img_width, img_height = info["file_name"].split(".")[0], info["width"], info["height"]

            for category in cls_info:
                if category["id"] == cls_id:
                    cls = category["name"]

            size = {
                "width": img_width,
                "height": img_height,
                "depth": "3"
            }

            bndbox = {
                "xmin": anno["bbox"][0],
                "ymin": anno["bbox"][1],
                "xmax": anno["bbox"][2],
                "ymax": anno["bbox"][3]
            }

            obj_info = {
                "name": cls,
                "bndbox": bndbox
            }

            if filename in data:
                obj_idx = str(int(data[filename]["objects"]["num_obj"])-1)
                data[filename]["objects"][str(obj_idx)] = obj_info
                data[filename]["objects"]["num_obj"] = int(data[filename]["objects"]["num_obj"]) + 1

            else:

                obj = {
                    "num_obj": "1",
                    "0": obj_info
                }

                data[filename] = {
                    "size": size,
                    "objects": obj
                }

            print(data)

            if cnt >100:
                break

            cnt+=1


        #print(json_data["images"])
        #print(json_data["categories"])



