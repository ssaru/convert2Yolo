import os
from xml.etree.ElementTree import dump
import json
import pprint

import argparse


from Format import VOC, COCO, UDACITY, KITTI, YOLO

parser = argparse.ArgumentParser(description='label Converting example.')
parser.add_argument('--datasets', type=str, help='type of datasets')
parser.add_argument('--img_path', type=str, help='directory of image folder')
parser.add_argument('--label', type=str, help='directory of label folder or label file path')
parser.add_argument('--convert_output_path', type=str, help='directory of label folder')
parser.add_argument('--img_type', type=str, help='type of image')
parser.add_argument('--manipast_path', type=str, help='directory of manipast file', default="./")
parser.add_argument('--cls_list_file', type=str, help='directory of *.names file', default="./")


args = parser.parse_args()


"""
voc = VOC()

path = "example/voc/label/"
#000001.xml

reaction, data = voc.parse(path)

#print(reaction, data)
#print()
#print()
#print()
#print()



reaction, xml_list = voc.generate(data)

#print(xml_list)
#print(reaction)
'''
for xml in xml_list:
    dump(xml_list[xml])
    print()
    print()
    print()
'''
#print()
#print()
#print()
#print()

reaction, msg =voc.save(xml_list, "result")

#print(reaction, msg)


from Format import COCO

coco = COCO()

result, data = coco.parse("instances_val2017.json")

#print(result)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(data)


udacity = UDACITY()

result, data = udacity.parse("/media/keti-1080ti/keti_martin/Martin/DataSet/Udacity/object detection/udacity/label/labels.csv", "/media/keti-1080ti/keti_martin/Martin/DataSet/Udacity/object detection/udacity/JPEG/")
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)


kitti = KITTI()

result, data = kitti.parse("/media/martin/Martin/DataSet/KITTI/Object_Detection_2D/data_object_label_2/training/label_2/", "/media/martin/Martin/DataSet/KITTI/Object_Detection_2D/data_object_image_2/training/image_2/")

print(data)

coco = COCO()
result, data = coco.parse("instances_val2017.json")

yolo = YOLO("coco.names")

result, data = yolo.generate(data)

result, data = yolo.save(data, "./yolo_test", "./", ".jpg", "./")

print(result)
print()
print(data)
"""

def main(config):

    if config["datasets"] == "VOC":
        voc = VOC()
        yolo = YOLO(os.path.abspath(config["cls_list"]))

        flag, data = voc.parse(config["label"])

        if flag == True:
            flag, data = voc.generate(data)

            if flag == True:
                flag, data = yolo.save(data, config["output_path"], config["img_path"] ,
                                        config["img_type"], config["manipast_path"])

                if flag == False:
                    print("Saving Result : {}, msg : {}".format(flag, data))

            else:
                print("YOLO Generating Result : {}, msg : {}".format(flag, data))

        else:
            print("VOC Parsing Result : {}, msg : {}".format(flag, data))


    elif config["dataasets"] == "COCO":
        coco = COCO()
        yolo = YOLO(os.path.abspath(config["cls_list"]))

        flag, data = coco.parse(config["label"])

        if flag == True:
            flag, data = yolo.generate(data)

            if flag == True:
                flag, data = yolo.save(data, config["output_path"], config["img_path"],
                                        config["img_type"], config["manipast_path"])

                if flag == False:
                    print("Saving Result : {}, msg : {}".format(flag, data))

            else:
                print("YOLO Generating Result : {}, msg : {}".format(flag, data))

        else:
            print("COCO Parsing Result : {}, msg : {}".format(flag, data))

    elif config["dataasets"] == "UDACITY":
        udacity = UDACITY()
        yolo = YOLO(os.path.abspath(config["cls_list"]))

        flag, data = udacity.parse(config["label"])

        if flag == True:
            flag, data = yolo.generate(data)

            if flag == True:
                flag, data = yolo.save(data, config["output_path"], config["img_path"],
                                       config["img_type"], config["manipast_path"])

                if flag == False:
                    print("Saving Result : {}, msg : {}".format(flag, data))

            else:
                print("UDACITY Generating Result : {}, msg : {}".format(flag, data))

        else:
            print("COCO Parsing Result : {}, msg : {}".format(flag, data))

    elif config["dataasets"] == "KITTI":
        kitti = KITTI()
        yolo = YOLO(os.path.abspath(config["cls_list"]))

        flag, data = kitti.parse(config["label"])

        if flag == True:
            flag, data = yolo.generate(data)

            if flag == True:
                flag, data = yolo.save(data, config["output_path"], config["img_path"],
                                       config["img_type"], config["manipast_path"])

                if flag == False:
                    print("Saving Result : {}, msg : {}".format(flag, data))

            else:
                print("YOLO Generating Result : {}, msg : {}".format(flag, data))

        else:
            print("KITTI Parsing Result : {}, msg : {}".format(flag, data))

    else:
        print("Unkwon Datasets")

if __name__ == '__main__':

    config ={
        "datasets": args.datasets,
        "img_path": args.img_path,
        "label": args.label,
        "img_type": args.img_type,
        "manipast_path": args.manipast_path,
        "output_path": args.convert_output_path,
        "cls_list": args.cls_list_file,
    }

    main(config)