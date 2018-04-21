from xml.etree.ElementTree import dump

from Format import VocPascal

voc = VocPascal()

path = "example/voc/label/000001.xml"

reaction, data = voc.parse(path)

print(data)
print(reaction)

reaction, xml = voc.generate(data)

dump(xml)
print(reaction)