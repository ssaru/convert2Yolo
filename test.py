
from xml.etree.ElementTree import dump

from Format import VocPascal

import os


voc = VocPascal()

path = "example/voc/label/"
#000001.xml

reaction, data = voc.parse(path)

print(reaction, data)
print()
print()
print()
print()



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
print()
print()
print()
print()

reaction, msg =voc.save(xml_list, "result")

#print(reaction, msg)


from Format import Coco

coco = Coco()

coco.parse("/media/keti-1080ti/Martin/DataSet/COCO/annotations_trainval2014/annotations/instances_train2014.json")

