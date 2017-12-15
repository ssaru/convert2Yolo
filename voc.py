from convert2Yolo import convert2Yolo
import sys


if __name__ == '__main__':

    print(sys.argv)

    class_path = "test.names"
    image_dir = "example/voc/JPEG/"
    anno_dir = "example/voc/label/"
    label_dir = "example/voc/results/"

    if len(sys.argv) < 4:
        print("need more parameter : [class file path] [jpeg file path] [annotation file path] [result file path]")
        print("it will process default parameter")
        print("default execute command is 'python3 voc.py test.names example/voc/JPEG/ example/voc/label/ example/voc/results/'")

    else:
        if sys.argv[1] is not None:
            class_path = sys.argv[1]
        if sys.argv[2] is not None:
            image_dir = sys.argv[2]
        if sys.argv[3] is not None:
            anno_dir = sys.argv[3]
        if sys.argv[4] is not None:
            label_dir = sys.argv[4]

    print("class_path : {}".format(class_path))
    print("image_dir : {}".format(image_dir))
    print("anno_dir : {}".format(anno_dir))
    print("label_dir : {}".format(label_dir))

    toYolo = convert2Yolo(classes_path = class_path, image_dir=image_dir, anno_dir=anno_dir, label_dir=label_dir)
    toYolo.parsingVocXML()