from convert2Yolo import convert2Yolo
import msgLogInfo
from voc.toYOLO import VocPascal as Voc2Yolo
import sys

if __name__ == '__main__':
    print("\n\n\n")
    if len(sys.argv) < 4:
        print("need more parameter : [class file path] [jpeg file path] [annotation file path] [result file path]")
        print("it will process default parameter")
        print("default execute command is 'python3 voc_example.py test.names example/voc/JPEG/ example/voc/label/ example/voc/results/'")
        exit()

    class_path = sys.argv[1]
    image_type = sys.argv[2]
    image_dir = sys.argv[3]
    anno_dir = sys.argv[4]
    label_dir = sys.argv[5]
    manifest_dir = sys.argv[6]

    print("class_path : {}".format(class_path))
    print("image_dir : {}".format(image_dir))
    print("anno_dir : {}".format(anno_dir))
    print("label_dir : {}".format(label_dir), end="\n\n\n")

    converter = convert2Yolo(classes_path = class_path, image_type= image_type, image_dir=image_dir, anno_dir=anno_dir, label_dir=label_dir, manifest_dir = manifest_dir )
    Voc2Yolo(converter)