import xml.etree.ElementTree as Et
from xml.etree.ElementTree import ElementTree

from base import base_reader


class XmlReader(base_reader.Reader):

    ALLOW_EXTENSION = "xml"

    def __init__(self) -> None:
        super(XmlReader, self).__init__()

    def __call__(self, xml_path: str) -> None or ElementTree:
        if not self._is_validated_file(xml_path):
            return None

        return self._load_xml(xml_path)

    def _is_validated_file(self, filename: str) -> bool:
        file_extension: str = filename.split(".")[-1].lower()

        if file_extension == XmlReader.ALLOW_EXTENSION:
            return True

        self.logger.warning("Warning: extension of file not supported. " + \
                            "this file skip. "
                            "Supported file extension following : " + \
                            "`{}`".format(XmlReader.ALLOW_EXTENSION))
        return False

    @staticmethod
    def _load_xml(filepath: str) -> ElementTree:
        with open(filepath) as xml:
            tree: ElementTree = Et.parse(xml)

        return tree


if __name__ == "__main__":
    xml_file_path = "../example/voc/label/000001.xml"
    wrong_file_path = "../example/voc/label/000001.jpeg"

    xml_reader = XmlReader()
    xml_tree = xml_reader(xml_file_path)
    print(xml_tree)

    result = xml_reader(wrong_file_path)
    print(result)