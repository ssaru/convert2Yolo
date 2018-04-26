import os
from xml.etree.ElementTree import dump
import json
import pprint

from Format import VOC, COCO, UDACITY



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
"""

udacity = UDACITY()

result, data = udacity.parse("/media/keti-1080ti/keti_martin/Martin/DataSet/Udacity/object detection/udacity/label/labels.csv", "/media/keti-1080ti/keti_martin/Martin/DataSet/Udacity/object detection/udacity/JPEG/")
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
