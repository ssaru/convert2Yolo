from xml.etree.ElementTree import dump

from Format import VocPascal

voc = VocPascal()

path = "example/voc/label/000001.xml"

data = voc.parse(path)

print(data)

xml = voc.generate(data)

dump(xml)