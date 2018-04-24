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
                    "folder" : <string>
                    "filename" : <string>                            
                    "size" :
                                {
                                    "width" : <string>
                                    "height" : <string>
                                    "depth" : <string>
                                }
                
                    "objects" :
                                {
                                    "num_obj" : <string>
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

                xml_folder = Element("folder")
                xml_folder.text = element["folder"]
                xml_annotation.append(xml_folder)

                xml_filename = Element("filename")
                xml_filename.text = element["filename"]
                xml_annotation.append(xml_filename)

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

                xml_list[element["filename"].split(".")[0]] = xml_annotation

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
                dump(xml)
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
                    "folder": root.find("folder").text,
                    "filename": root.find("filename").text,
                    "size": size,
                    "objects": obj
                }

                data[annotation["filename"].split(".")[0]] = annotation

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

    def __init__(self):
        self.cls_list = {'1': 'person',
                         '2': 'bicycle',
                         '3': 'car',
                         '4': 'motorcycle',
                         '5': 'airplane',
                         '6': 'bus',
                         '7': 'train',
                         '8': 'truck',
                         '9': 'boat',
                         '10': 'traffic_light',
                         '11': 'fire_hydrant',
                         '12': 'unknown',
                         '13': 'stop_sign',
                         '14': 'parking_meter',
                         '15': 'bench',
                         '16': 'bird',
                         '17': 'cat',
                         '18': 'dog',
                         '19': 'horse',
                         '20': 'sheep',
                         '21': 'cow',
                         '22': 'elephant',
                         '23': 'bear',
                         '24': 'zebra',
                         '25': 'giraffe',
                         '26': 'unknown',
                         '27': 'backpack',
                         '28': 'umbrella',
                         '29': 'unknown',
                         '30': 'unknown',
                         '31': 'handbag',
                         '32': 'tie',
                         '33': 'suitcase',
                         '34': 'frisbee',
                         '35': 'skis',
                         '36': 'snowboard',
                         '37': 'sports_ball',
                         '38': 'kite',
                         '39': 'baseball_bat',
                         '40': 'baseball_glove',
                         '41': 'skateboard',
                         '42': 'surfboard',
                         '43': 'tennis_racket',
                         '44': 'bottle',
                         '45': 'unknown',
                         '46': 'wine_glass',
                         '47': 'cup',
                         '48': 'fork',
                         '49': 'knife',
                         '50': 'spoon',
                         '51': 'bowl',
                         '52': 'banana',
                         '53': 'apple',
                         '54': 'sandwich',
                         '55': 'orange',
                         '56': 'broccoli',
                         '57': 'carrot',
                         '58': 'hot_dog',
                         '59': 'pizza',
                         '60': 'donut',
                         '61': 'cake',
                         '62': 'chair',
                         '63': 'couch',
                         '64': 'potted_plant',
                         '65': 'bed',
                         '66': 'unknown',
                         '67': 'dining_table',
                         '68': 'unknown',
                         '69': 'unknown',
                         '70': 'toilet',
                         '71': 'unknown',
                         '72': 'tv',
                         '73': 'laptop',
                         '74': 'mouse',
                         '75': 'remote',
                         '76': 'keyboard',
                         '77': 'cell_phone',
                         '78': 'microwave',
                         '79': 'oven',
                         '80': 'toaster',
                         '81': 'sink',
                         '82': 'refrigerator',
                         '83': 'unknown',
                         '84': 'book',
                         '85': 'clock',
                         '86': 'vase',
                         '87': 'scissors',
                         '88': 'teddy_bear',
                         '89': 'hair_drier',
                         '90': 'toothbrush',
                         }

    def parse(self,path):
        json_data = json.load(open(path))

        data = {}

        for anno in json_data["annotations"]:

            image_id = anno["image_id"]
            image_name = str(anno["image_id"]).zfill(12)
            cls_idx = str(anno["category_id"])
            cls = str(self.cls_list[cls_idx])
            box = [int(anno["bbox"][0]),int(anno["bbox"][1]), int(anno["bbox"][2]), int(anno["bbox"][3])]

            obj = {
                "name": cls,
                "box": box
            }

        