from convert2Yolo import convert2Yolo

toYolo = convert2Yolo(classes_path = "udacity.names")
toYolo.Udacity2Voc()


'''
def indent(elem, level=0):
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


tree = parse("note.xml")
annotation = tree.getroot()

xml_object = Element("object")

xml_name = Element("name")
xml_name.text=" "
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
xml_xmin.text = " "
xml_bndbox.append(xml_xmin)


xml_ymin = Element("ymin")
xml_ymin.text = " "
xml_bndbox.append(xml_ymin)

xml_xmax = Element("xmax")
xml_xmax.text = " "
xml_bndbox.append(xml_xmax)

xml_ymax = Element("ymax")
xml_ymax.text = " "
xml_bndbox.append(xml_ymax)
xml_object.append(xml_bndbox)

annotation.append(xml_object)
indent(annotation)
dump(annotation)



xml_annotation = Element("annotation")

xml_folder = Element("folder")
xml_folder.text = "udacity"

xml_annotation.append(xml_folder)

xml_filename = Element("filename")
xml_filename.text = " "
xml_annotation.append(xml_filename)

xml_path = Element("path")
xml_path.text= " "
xml_annotation.append(xml_path)

xml_source = Element("source")

xml_database = Element("database")
xml_database.text = "Unknown"
xml_source.append(xml_database)
xml_annotation.append(xml_source)

xml_size = Element("size")
xml_width = Element("width")
xml_width.text=" "
xml_size.append(xml_width)

xml_height = Element("height")
xml_height.text = " "
xml_size.append(xml_height)

xml_depth = Element("depth")
xml_depth.text = " "
xml_size.append(xml_depth)

xml_annotation.append(xml_size)

xml_segmented = Element("segmented")
xml_segmented.text = "0"

xml_annotation.append(xml_segmented)

xml_object = Element("object")

xml_name = Element("name")
xml_name.text=" "
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
xml_xmin.text = " "
xml_bndbox.append(xml_xmin)


xml_ymin = Element("ymin")
xml_ymin.text = " "
xml_bndbox.append(xml_ymin)

xml_xmax = Element("xmax")
xml_xmax.text = " "
xml_bndbox.append(xml_xmax)

xml_ymax = Element("ymax")
xml_ymax.text = " "
xml_bndbox.append(xml_ymax)
xml_object.append(xml_bndbox)

xml_annotation.append(object)



indent(xml_annotation)
dump(xml_annotation)
ElementTree(xml_annotation).write("note.xml")
'''