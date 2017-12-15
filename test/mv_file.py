import os
from os import walk, getcwd
from shutil import copyfile
from shutil import move

class color:
    BOLD = '\033[1m'
    END = '\033[0m'
    DEFAULT = '\033[0;37;40m'
    RED = '\033[91m'

# Configure Paths
number = 200

base_path = "/media/martin/enumcut/EnumNet/EnumCut/DataSet/NSFW/ImageData/"
img_path = base_path+"JPEG/"
label_path = base_path+"label/"

save_base = "/media/martin/enumcut/EnumNet/EnumCut/DataSet/NSFW/ImageData/finished/"
save_img_path = save_base + "JPEG/"
save_label_path = save_base + "label/"

img_list = []
label_list = []

for (dirpath, dirnames, filenames) in walk(label_path):
    label_list.extend(filenames)
    break

for (dirpath, dirnames, filenames) in walk(img_path):
    img_list.extend(filenames)
    break

img_list.sort()
label_list.sort()

print("img list : {}".format(img_path))
print("label list :{}".format(label_path))
print()


print("img list : {}".format(img_list))
print("label list : {}".format(label_list))
print()
#print(img_list[0][0:-4])

try:
    for j in range(0, len(label_list)):
        for i in range(0, len(img_list)):

            #if os.path.exists(label_path + label_list[j]) and os.path.exists(img_path + img_list[i]) :

            if(label_list[j][0:-4] == img_list[i][0:-4]):
                print(label_list[j])
                print(img_list[i])
                print()
                copyfile(img_path+img_list[i], save_img_path+img_list[i])
                copyfile(label_path + label_list[j], save_label_path + label_list[j])
            else:
                pass
                #raise Exception("image file doesn't exist : {}".format(label_list[i]))
            '''
            if os.path.exists(label_path + label_list[i]):
                if (img_list[i][0:-4] == label_list[j][0:-4]):
                    move(label_path + label_list[i], save_label_path + label_list[i])

            else:
                raise Exception("image file doesn't exist : {}".format(label_list[i]))
            '''

except Exception as e:
    print(color.BOLD + color.RED + "ERROR : {}".format(e) + color.END)

