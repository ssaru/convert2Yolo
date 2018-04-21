import sys
import os

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree

"""
Common Data format

{
    "folder" : <string>
    "filename" : <string>
    "source" :
                {
                    "database" : <string>
                }
    "path" : <string>

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

class VocPascal():
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

    def generate(self, element):
        try:
            xml_annotation = Element("annotation")

            xml_folder = Element("folder")
            xml_folder.text = element["folder"]
            xml_annotation.append(xml_folder)

            xml_filename = Element("filename")
            xml_filename.text = element["filename"]
            xml_annotation.append(xml_filename)

            xml_path = Element("path")
            xml_path.text = element["path"]
            xml_annotation.append(xml_path)

            xml_source = Element("source")

            xml_database = Element("database")
            xml_database.text = element["source"]["database"]
            xml_source.append(xml_database)
            xml_annotation.append(xml_source)

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

            xml_object = Element("object")

            if int(element["objects"]["num_obj"]) < 1:
                return False, "number of Object less than 1"

            for i in range(0, int(element["objects"]["num_obj"])):
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

            return True, xml_annotation
        except Exception as e:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            msg = "ERROR : {}, moreInfo : {}\t{}\t{}".format(e, exc_type, fname, exc_tb.tb_lineno)

            return False, msg

    def save(self, xml, path):

        try:
            ElementTree(xml).write(path)
            return True, None

        except Exception as e:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            msg = "ERROR : {}, moreInfo : {}\t{}\t{}".format(e, exc_type, fname, exc_tb.tb_lineno)

            return False, msg

    def parse(self, path):
        try:
            annotation = {}

            xml = open(path, "r")

            tree = ET.parse(xml)
            root = tree.getroot()

            annotation["folder"] = root.find("folder").text
            annotation["filename"] = root.find("filename").text

            source = {}
            xml_source = root.find("source")
            source["database"] = xml_source.find("database").text
            annotation["source"] = source

            annotation["path"] = root.find("path").text

            size = {}
            xml_size = root.find("size")
            size["width"] = xml_size.find("width").text
            size["height"] = xml_size.find("height").text
            size["depth"] = xml_size.find("depth").text

            annotation["size"] = size

            objects = root.findall("object")

            if len(objects) == 0:
                return None

            obj = {}
            obj["num_obj"] = len(objects)

            obj_index = 0
            for _object in objects:
                tmp = {}
                bndbox = {}
                tmp["name"] = _object.find("name").text

                xml_bndbox = _object.find("bndbox")

                bndbox["xmin"] = xml_bndbox.find("xmin").text
                bndbox["ymin"] = xml_bndbox.find("ymin").text
                bndbox["xmax"] = xml_bndbox.find("xmax").text
                bndbox["ymax"] = xml_bndbox.find("ymax").text
                tmp["bndbox"] = bndbox

                obj[str(obj_index)] = tmp
                obj_index += 1

            annotation["objects"] = obj

            return True, annotation

        except Exception as e:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            msg = "ERROR : {}, moreInfo : {}\t{}\t{}".format(e, exc_type, fname, exc_tb.tb_lineno)

            return False, msg



