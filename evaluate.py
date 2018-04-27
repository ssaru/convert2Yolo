import os
import argparse
import time
import pprint

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import json

from Format import VOC, COCO, UDACITY, KITTI

parser = argparse.ArgumentParser(description='Evaluate label Converting.')
parser.add_argument('--datasets', type=str, help='type of datasets', default='KITTI')
parser.add_argument('--img_path', type=str, help='directory of image folder', default="/media/martin/Martin/DataSet/KITTI/Object_Detection_2D/data_object_image_2/training/image_2/")
parser.add_argument('--label_path', type=str, help='directory of label folder', default="/media/martin/Martin/DataSet/KITTI/Object_Detection_2D/data_object_label_2/training/label_2/")
parser.add_argument('--img_type', type=str, help='type of image', default='.png')


args = parser.parse_args()

def main():
    pp = pprint.PrettyPrinter(indent=4)

    img_path = args.img_path
    label_path = args.label_path
    img_type = args.img_type
    datasets = args.datasets

    result = None
    data = None

    if datasets is "COCO":
        coco = COCO()
        result, data = coco.parse(label_path)
    elif datasets is "VOC":
        voc = VOC()
        result, data = voc.parse(label_path)
    elif datasets is "UDACITY":
        udacity = UDACITY()
        result, data = udacity.parse(label_path, img_path)
    elif datasets is "KITTI":
        kitti = KITTI()
        result, data = kitti.parse(label_path, img_path)



    if result is True:
        for key in data:

            filepath = "".join([img_path, key, img_type])
            im = Image.open(filepath)

            draw = ImageDraw.Draw(im)
            print("data['{}']: ".format(key), end="")
            pp.pprint(data[key])
            print("num_object : {}".format(data[key]["objects"]["num_obj"]))
            for idx in range(0, int(data[key]["objects"]["num_obj"])):
                print("idx {}, name : {}, bndbox :{}".format(idx, data[key]["objects"][str(idx)]["name"], data[key]["objects"][str(idx)]["bndbox"]))

                x0 = data[key]["objects"][str(idx)]["bndbox"]["xmin"]
                y0 = data[key]["objects"][str(idx)]["bndbox"]["ymin"]
                x1 = data[key]["objects"][str(idx)]["bndbox"]["xmax"]
                y1 = data[key]["objects"][str(idx)]["bndbox"]["ymax"]

                draw.rectangle(((x0,y0), (x1,y1)), outline='#00ff88')
                draw.text((x0,y0), data[key]["objects"][str(idx)]["name"])

            del draw
            print("===============================================================================================\n\n")
            plt.imshow(im)
            plt.show()
            plt.clf()
            im.close()

    else:
        print("return value : {}, msg : {}".format(result, data))

if __name__ == '__main__':
    main()