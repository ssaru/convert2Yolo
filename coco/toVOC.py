#-*- coding: utf-8 -*-

import json
from pprint import pprint
import cv2
import time


"""

{'annotations': [{'area': 54652.9556,
                  'bbox': [116.95, 305.86, 285.3, 266.03],
                  'category_id': 58,
                  'id': 86,
                  'image_id': 480023,
                  'iscrowd': 0,
                  'segmentation': [[312.29,
                                    562.89,
                                    402.25,
                                    511.49,
                                    400.96,
                                    425.38,
                                    398.39,
                                    372.69,
                                    388.11,
                                    332.85,
                                    318.71,
                                    325.14,
                                    295.58,
                                    305.86,
                                    269.88,
                                    314.86,
                                    258.31,
                                    337.99,
                                    217.19,
                                    321.29,
                                    182.49,
                                    343.13,
                                    141.37,
                                    348.27,
                                    132.37,
                                    358.55,
                                    159.36,
                                    377.83,
                                    116.95,
                                    421.53,
                                    167.07,
                                    499.92,
                                    232.61,
                                    560.32,
                                    300.72,
                                    571.89]]}

http://images.cocodataset.org/test2014/COCO_test2014_000000540552.jpg

[{'id': 1, 'name': 'person', 'supercategory': 'person'},
                {'id': 2, 'name': 'bicycle', 'supercategory': 'vehicle'},
                {'id': 3, 'name': 'car', 'supercategory': 'vehicle'},
                {'id': 4, 'name': 'motorcycle', 'supercategory': 'vehicle'},
                {'id': 5, 'name': 'airplane', 'supercategory': 'vehicle'},
                {'id': 6, 'name': 'bus', 'supercategory': 'vehicle'},
                {'id': 7, 'name': 'train', 'supercategory': 'vehicle'},
                {'id': 8, 'name': 'truck', 'supercategory': 'vehicle'},
                {'id': 9, 'name': 'boat', 'supercategory': 'vehicle'},
                {'id': 10, 'name': 'traffic light', 'supercategory': 'outdoor'},
                {'id': 11, 'name': 'fire hydrant', 'supercategory': 'outdoor'},
                {'id': 13, 'name': 'stop sign', 'supercategory': 'outdoor'},
                {'id': 14, 'name': 'parking meter', 'supercategory': 'outdoor'},
                {'id': 15, 'name': 'bench', 'supercategory': 'outdoor'},
                {'id': 16, 'name': 'bird', 'supercategory': 'animal'},
                {'id': 17, 'name': 'cat', 'supercategory': 'animal'},
                {'id': 18, 'name': 'dog', 'supercategory': 'animal'},
                {'id': 19, 'name': 'horse', 'supercategory': 'animal'},
                {'id': 20, 'name': 'sheep', 'supercategory': 'animal'},
                {'id': 21, 'name': 'cow', 'supercategory': 'animal'},
                {'id': 22, 'name': 'elephant', 'supercategory': 'animal'},
                {'id': 23, 'name': 'bear', 'supercategory': 'animal'},
                {'id': 24, 'name': 'zebra', 'supercategory': 'animal'},
                {'id': 25, 'name': 'giraffe', 'supercategory': 'animal'},
                {'id': 27, 'name': 'backpack', 'supercategory': 'accessory'},
                {'id': 28, 'name': 'umbrella', 'supercategory': 'accessory'},
                {'id': 31, 'name': 'handbag', 'supercategory': 'accessory'},
                {'id': 32, 'name': 'tie', 'supercategory': 'accessory'},
                {'id': 33, 'name': 'suitcase', 'supercategory': 'accessory'},
                {'id': 34, 'name': 'frisbee', 'supercategory': 'sports'},
                {'id': 35, 'name': 'skis', 'supercategory': 'sports'},
                {'id': 36, 'name': 'snowboard', 'supercategory': 'sports'},
                {'id': 37, 'name': 'sports ball', 'supercategory': 'sports'},
                {'id': 38, 'name': 'kite', 'supercategory': 'sports'},
                {'id': 39, 'name': 'baseball bat', 'supercategory': 'sports'},
                {'id': 40, 'name': 'baseball glove', 'supercategory': 'sports'},
                {'id': 41, 'name': 'skateboard', 'supercategory': 'sports'},
                {'id': 42, 'name': 'surfboard', 'supercategory': 'sports'},
                {'id': 43, 'name': 'tennis racket', 'supercategory': 'sports'},
                {'id': 44, 'name': 'bottle', 'supercategory': 'kitchen'},
                {'id': 46, 'name': 'wine glass', 'supercategory': 'kitchen'},
                {'id': 47, 'name': 'cup', 'supercategory': 'kitchen'},
                {'id': 48, 'name': 'fork', 'supercategory': 'kitchen'},
                {'id': 49, 'name': 'knife', 'supercategory': 'kitchen'},
                {'id': 50, 'name': 'spoon', 'supercategory': 'kitchen'},
                {'id': 51, 'name': 'bowl', 'supercategory': 'kitchen'},
                {'id': 52, 'name': 'banana', 'supercategory': 'food'},
                {'id': 53, 'name': 'apple', 'supercategory': 'food'},
                {'id': 54, 'name': 'sandwich', 'supercategory': 'food'},
                {'id': 55, 'name': 'orange', 'supercategory': 'food'},
                {'id': 56, 'name': 'broccoli', 'supercategory': 'food'},
                {'id': 57, 'name': 'carrot', 'supercategory': 'food'},
                {'id': 58, 'name': 'hot dog', 'supercategory': 'food'},
                {'id': 59, 'name': 'pizza', 'supercategory': 'food'},
                {'id': 60, 'name': 'donut', 'supercategory': 'food'},
                {'id': 61, 'name': 'cake', 'supercategory': 'food'},
                {'id': 62, 'name': 'chair', 'supercategory': 'furniture'},
                {'id': 63, 'name': 'couch', 'supercategory': 'furniture'},
                {'id': 64,
                 'name': 'potted plant',
                 'supercategory': 'furniture'},
                {'id': 65, 'name': 'bed', 'supercategory': 'furniture'},
                {'id': 67,
                 'name': 'dining table',
                 'supercategory': 'furniture'},
                {'id': 70, 'name': 'toilet', 'supercategory': 'furniture'},
                {'id': 72, 'name': 'tv', 'supercategory': 'electronic'},
                {'id': 73, 'name': 'laptop', 'supercategory': 'electronic'},
                {'id': 74, 'name': 'mouse', 'supercategory': 'electronic'},
                {'id': 75, 'name': 'remote', 'supercategory': 'electronic'},
                {'id': 76, 'name': 'keyboard', 'supercategory': 'electronic'},
                {'id': 77, 'name': 'cell phone', 'supercategory': 'electronic'},
                {'id': 78, 'name': 'microwave', 'supercategory': 'appliance'},
                {'id': 79, 'name': 'oven', 'supercategory': 'appliance'},
                {'id': 80, 'name': 'toaster', 'supercategory': 'appliance'},
                {'id': 81, 'name': 'sink', 'supercategory': 'appliance'},
                {'id': 82,
                 'name': 'refrigerator',
                 'supercategory': 'appliance'},
                {'id': 84, 'name': 'book', 'supercategory': 'indoor'},
                {'id': 85, 'name': 'clock', 'supercategory': 'indoor'},
                {'id': 86, 'name': 'vase', 'supercategory': 'indoor'},
                {'id': 87, 'name': 'scissors', 'supercategory': 'indoor'},
                {'id': 88, 'name': 'teddy bear', 'supercategory': 'indoor'},
                {'id': 89, 'name': 'hair drier', 'supercategory': 'indoor'},
                {'id': 90, 'name': 'toothbrush', 'supercategory': 'indoor'}],

{'id': 1, 'name': 'person', 'supercategory': 'person'},
                {'id': 2, 'name': 'bicycle', 'supercategory': 'vehicle'},
                {'id': 3, 'name': 'car', 'supercategory': 'vehicle'},
                {'id': 4, 'name': 'motorcycle', 'supercategory': 'vehicle'},
                {'id': 5, 'name': 'airplane', 'supercategory': 'vehicle'},
                {'id': 6, 'name': 'bus', 'supercategory': 'vehicle'},
                {'id': 7, 'name': 'train', 'supercategory': 'vehicle'},
                {'id': 8, 'name': 'truck', 'supercategory': 'vehicle'},
                {'id': 9, 'name': 'boat', 'supercategory': 'vehicle'},
                {'id': 10, 'name': 'traffic light', 'supercategory': 'outdoor'},
                {'id': 11, 'name': 'fire hydrant', 'supercategory': 'outdoor'},
                {'id': 13, 'name': 'stop sign', 'supercategory': 'outdoor'},
                {'id': 14, 'name': 'parking meter', 'supercategory': 'outdoor'},
                {'id': 15, 'name': 'bench', 'supercategory': 'outdoor'},
                {'id': 16, 'name': 'bird', 'supercategory': 'animal'},
                {'id': 17, 'name': 'cat', 'supercategory': 'animal'},
                {'id': 18, 'name': 'dog', 'supercategory': 'animal'},
                {'id': 19, 'name': 'horse', 'supercategory': 'animal'},
                {'id': 20, 'name': 'sheep', 'supercategory': 'animal'},
                {'id': 21, 'name': 'cow', 'supercategory': 'animal'},
                {'id': 22, 'name': 'elephant', 'supercategory': 'animal'},
                {'id': 23, 'name': 'bear', 'supercategory': 'animal'},
                {'id': 24, 'name': 'zebra', 'supercategory': 'animal'},
                {'id': 25, 'name': 'giraffe', 'supercategory': 'animal'},
                {'id': 27, 'name': 'backpack', 'supercategory': 'accessory'},
                {'id': 28, 'name': 'umbrella', 'supercategory': 'accessory'},
                {'id': 31, 'name': 'handbag', 'supercategory': 'accessory'},
                {'id': 32, 'name': 'tie', 'supercategory': 'accessory'},
                {'id': 33, 'name': 'suitcase', 'supercategory': 'accessory'},
                {'id': 34, 'name': 'frisbee', 'supercategory': 'sports'},
                {'id': 35, 'name': 'skis', 'supercategory': 'sports'},
                {'id': 36, 'name': 'snowboard', 'supercategory': 'sports'},
                {'id': 37, 'name': 'sports ball', 'supercategory': 'sports'},
                {'id': 38, 'name': 'kite', 'supercategory': 'sports'},
                {'id': 39, 'name': 'baseball bat', 'supercategory': 'sports'},
                {'id': 40, 'name': 'baseball glove', 'supercategory': 'sports'},
                {'id': 41, 'name': 'skateboard', 'supercategory': 'sports'},
                {'id': 42, 'name': 'surfboard', 'supercategory': 'sports'},
                {'id': 43, 'name': 'tennis racket', 'supercategory': 'sports'},
                {'id': 44, 'name': 'bottle', 'supercategory': 'kitchen'},
                {'id': 46, 'name': 'wine glass', 'supercategory': 'kitchen'},
                {'id': 47, 'name': 'cup', 'supercategory': 'kitchen'},
                {'id': 48, 'name': 'fork', 'supercategory': 'kitchen'},
                {'id': 49, 'name': 'knife', 'supercategory': 'kitchen'},
                {'id': 50, 'name': 'spoon', 'supercategory': 'kitchen'},
                {'id': 51, 'name': 'bowl', 'supercategory': 'kitchen'},
                {'id': 52, 'name': 'banana', 'supercategory': 'food'},
                {'id': 53, 'name': 'apple', 'supercategory': 'food'},
                {'id': 54, 'name': 'sandwich', 'supercategory': 'food'},
                {'id': 55, 'name': 'orange', 'supercategory': 'food'},
                {'id': 56, 'name': 'broccoli', 'supercategory': 'food'},
                {'id': 57, 'name': 'carrot', 'supercategory': 'food'},
                {'id': 58, 'name': 'hot dog', 'supercategory': 'food'},
                {'id': 59, 'name': 'pizza', 'supercategory': 'food'},
                {'id': 60, 'name': 'donut', 'supercategory': 'food'},
                {'id': 61, 'name': 'cake', 'supercategory': 'food'},
                {'id': 62, 'name': 'chair', 'supercategory': 'furniture'},
                {'id': 63, 'name': 'couch', 'supercategory': 'furniture'},
                {'id': 64,
                 'name': 'potted plant',
                 'supercategory': 'furniture'},
                {'id': 65, 'name': 'bed', 'supercategory': 'furniture'},
                {'id': 67,
                 'name': 'dining table',
                 'supercategory': 'furniture'},
                {'id': 70, 'name': 'toilet', 'supercategory': 'furniture'},
                {'id': 72, 'name': 'tv', 'supercategory': 'electronic'},
                {'id': 73, 'name': 'laptop', 'supercategory': 'electronic'},
                {'id': 74, 'name': 'mouse', 'supercategory': 'electronic'},
                {'id': 75, 'name': 'remote', 'supercategory': 'electronic'},
                {'id': 76, 'name': 'keyboard', 'supercategory': 'electronic'},
                {'id': 77, 'name': 'cell phone', 'supercategory': 'electronic'},
                {'id': 78, 'name': 'microwave', 'supercategory': 'appliance'},
                {'id': 79, 'name': 'oven', 'supercategory': 'appliance'},
                {'id': 80, 'name': 'toaster', 'supercategory': 'appliance'},
                {'id': 81, 'name': 'sink', 'supercategory': 'appliance'},
                {'id': 82,
                 'name': 'refrigerator',
                 'supercategory': 'appliance'},
                {'id': 84, 'name': 'book', 'supercategory': 'indoor'},
                {'id': 85, 'name': 'clock', 'supercategory': 'indoor'},
                {'id': 86, 'name': 'vase', 'supercategory': 'indoor'},
                {'id': 87, 'name': 'scissors', 'supercategory': 'indoor'},
                {'id': 88, 'name': 'teddy bear', 'supercategory': 'indoor'},
                {'id': 89, 'name': 'hair drier', 'supercategory': 'indoor'},
                {'id': 90, 'name': 'toothbrush', 'supercategory': 'indoor'}]

"""

class_list = {'1'    :   'person',
           '2'    :   'bicycle',
           '3'    :   'car',
           '4'    :   'motorcycle',
           '5'    :   'airplane',
           '6'    :   'bus',
           '7'    :   'train',
           '8'    :   'truck',
           '9'    :   'boat',
           '10'   :   'traffic_light',
           '11'   :   'fire_hydrant',
           '12'   :   'unknown',
           '13'   :   'stop_sign',
           '14'   :   'parking_meter',
           '15'   :   'bench',
           '16'   :   'bird',
           '17'   :   'cat',
           '18'   :   'dog',
           '19'   :   'horse',
           '20'   :   'sheep',
           '21'   :   'cow',
           '22'   :   'elephant',
           '23'   :   'bear',
           '24'   :   'zebra',
           '25'   :   'giraffe',
           '26'   :   'unknown',
           '27'   :   'backpack',
           '28'   :   'umbrella',
           '29'   :   'unknown',
           '30'   :   'unknown',
           '31'   :   'handbag',
           '32'   :   'tie',
           '33'   :   'suitcase',
           '34'   :   'frisbee',
           '35'   :   'skis',
           '36'   :   'snowboard',
           '37'   :   'sports_ball',
           '38'   :   'kite',
           '39'   :   'baseball_bat',
           '40'   :   'baseball_glove',
           '41'   :   'skateboard',
           '42'   :   'surfboard',
           '43'   :   'tennis_racket',
           '44'   :   'bottle',
           '45'   :   'unknown',
           '46'   :   'wine_glass',
           '47'   :   'cup',
           '48'   :   'fork',
           '49'   :   'knife',
           '50'   :   'spoon',
           '51'   :   'bowl',
           '52'   :   'banana',
           '53'   :   'apple',
           '54'   :   'sandwich',
           '55'   :   'orange',
           '56'   :   'broccoli',
           '57'   :   'carrot',
           '58'   :   'hot_dog',
           '59'   :   'pizza',
           '60'   :   'donut',
           '61'   :   'cake',
           '62'   :   'chair',
           '63'   :   'couch',
           '64'   :   'potted_plant',
           '65'   :   'bed',
           '66'   :   'unknown',
           '67'   :   'dining_table',
           '68'   :   'unknown',
           '69'   :   'unknown',
           '70'   :   'toilet',
           '71'   :   'unknown',
           '72'   :   'tv',
           '73'   :   'laptop',
           '74'   :   'mouse',
           '75'   :   'remote',
           '76'   :   'keyboard',
           '77'   :   'cell_phone',
           '78'   :   'microwave',
           '79'   :   'oven',
           '80'   :   'toaster',
           '81'   :   'sink',
           '82'   :   'refrigerator',
           '83'   :   'unknown',
           '84'   :   'book',
           '85'   :   'clock',
           '86'   :   'vase',
           '87'   :   'scissors',
           '88'   :   'teddy_bear',
           '89'   :   'hair_drier',
           '90'   :   'toothbrush',
           '91'   :   'unknown',
           '92'   :   'unknown',
           '93'   :   'unknown',
           '94'   :   'unknown',
           '95'   :   'unknown',
           '96'   :   'unknown',
           '97'   :   'unknown',
           '98'   :   'unknown',
           '99'   :   'unknown',
            }

data = json.load(open('/media/keti-1080ti/ketiCar/handling_DataSet/COCO/annotations/instances_train2014.json'))

root_path = "/media/keti-1080ti/ketiCar/handling_DataSet/COCO/train2014/"
file_meta = "COCO_train2014_"

font = cv2.FONT_HERSHEY_SIMPLEX

image_list = []

while True:

    count = 0

    for anno in data["annotations"]:

        if len(image_list) == 0:
            flag = False
        else:
            for i in image_list:
                if(anno["image_id"] == i):
                    flag = True
                else:
                    flag = False

        if flag == False:

            prop = {}
            obj = {}

            image_list.append(anno["image_id"])

            obj_cnt = 1

            image_id = str(anno["image_id"]).zfill(12)
            image_name = file_meta + image_id + ".jpg"
            image_file = root_path + image_name
            cls_idx = str(anno['category_id'])
            cls = str(class_list[cls_idx])
            box = [int(anno["bbox"][0]),int(anno["bbox"][1]), int(anno["bbox"][2]), int(anno["bbox"][3])]

            obj["name"] = cls
            obj["box"] = box

            prop["object" + str(obj_cnt)] = obj

            for aux_anno in data["annotations"]:

                aux_cls_idx = str(aux_anno['category_id'])
                aux_cls = str(class_list[aux_cls_idx])
                aux_box = [int(aux_anno["bbox"][0]), int(aux_anno["bbox"][1]), int(aux_anno["bbox"][2]), int(aux_anno["bbox"][3])]

                x_flag = (int(anno["bbox"][0]) == aux_box[0])
                y_flag = (int(anno["bbox"][1]) == aux_box[1])
                width_flag = (int(anno["bbox"][2]) == aux_box[2])
                height_flag = (int(anno["bbox"][3]) == aux_box[3])

                coord_flag = ((x_flag == True) and (y_flag == True) and (width_flag == True) and (height_flag == True))

                if(len(image_list) == 0):
                    image_same_flag = False

                for i in image_list:
                    if(aux_anno["image_id"] == i):
                        image_same_flag = True
                        #print("origin : {}, compare :{}".format(str(anno["image_id"]) ,str(aux_anno["image_id"])))
                        #print("coord_flag : {}".format(coord_flag))
                        #print("o_box : {}, c_box : {}".format(anno["bbox"], aux_anno["bbox"]))
                        #print("o_box : {}, c_box : {}".format(box, aux_box))

                    else:
                        image_same_flag = False

                if (image_same_flag == True):
                    if (coord_flag == False):
                        aux_obj = {}

                        obj_cnt += 1

                        aux_obj["name"] = aux_cls
                        aux_obj["box"] = aux_box
                        prop["object" + str(obj_cnt)] = aux_obj

        print(prop)

        img = cv2.imread(image_file)

        for _obj in prop.keys():

            _name = prop[_obj]["name"]
            _box = prop[_obj]["box"]

            _x = _box[0]
            _y = _box[1]
            _w = _box[2]
            _h = _box[3]

            img = cv2.rectangle(img, (_x, _y), (_x + _w, _y + _h), (0, 255, 0), 3)
            cv2.putText(img, _name, (_x, _y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            pass

        cv2.imshow("test", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


        '''
        print("idx : {}".format(anno['category_id']))





        print("cls : {}, id : {}, type: {}".format(cls, anno['id'], type(anno['id'])))

        img = cv2.imread(image_file)
        img = cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),3)
        cv2.putText(img, cls, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)


        print("image file : {}".format(image_file))

        cv2.imshow("test" ,img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        count += 1

        if count == 100 :
            exit()
        '''
        time.sleep(1)
