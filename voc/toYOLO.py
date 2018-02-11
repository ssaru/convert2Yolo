
from msgLogInfo import color
import os
import xml.etree.ElementTree as ET
from PIL import Image

class bcolors:
    HEADER    = '\033[95m'
    MARGENTA  = '\033[35m'
    BLUE      = '\033[34m'
    YELLOW    = '\033[33m'
    GREEN     = '\033[32m'
    RED       = '\033[31m'
    CYAN      = '\033[36m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger(bcolors):


    def __init__(self, mode = 'save', output_dir = ""):

        self.msg_degree = {
                'general'   :   "",
                'notice'    :   self.HEADER + self.BOLD +self.GREEN,
                'warning'   :   self.BOLD + self.WARNING,
                'fail'      :   self.BOLD + self.FAIL,
                }

        self.mode = mode

        if self.mode is 'save':
            self.log = open(output_dir + 'log_convert.txt', 'w')


    def __del__(self):
        if self.mode is 'save':
            self.log.close()


    def seperate(self, degree, seperator="-"):
        if self.mode is 'save':
            self.log.writelines(self.msg_degree[degree] + (seperator * 65) + self.ENDC)
        print(self.msg_degree[degree] + (seperator * 65) + self.ENDC)


    def put(self, degree, msg):
        if self.mode is 'save':
            self.log.writelines(self.msg_degree[degree] + msg + self.ENDC)
        print(self.msg_degree[degree] + msg + self.ENDC)


def get_file_list(dir):
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(dir):
        file_list.extend(filenames)
    return file_list



def VocPascal(converter):

    anno_dir = converter.anno_dir
    image_dir = converter.image_dir
    output_dir = converter.output_dir
    classes = converter.classes
    convertCoordinate = converter.convertCoordinate
    image_type = converter.image_type
    manifest_dir = converter.manifest_dir

    logger = Logger(mode = 'save', output_dir = manifest_dir)

    ##########################################
    # Make manifest file                     #
    ##########################################
    manifest = open(manifest_dir + 'manifest.txt', 'w')

    ##########################################
    # Get annotation file list               #
    ##########################################
    xml_list = get_file_list(anno_dir)

    ##########################################
    # read status Logging                    #
    ##########################################
    logger.seperate(degree='notice')
    logger.put(degree='notice', msg = "Start Converting")
    logger.seperate(degree='notice')
    logger.put(degree='notice', msg = "\n\n")
    logger.put(degree='general', msg = "xml file list : {}".format(xml_list))

    ##########################################
    # Start Processing                       #
    ##########################################
    try:
        for xml_name in xml_list:
            logger.put(degree='notice', msg="------------------------- Start XML Parsing -------------------------")

            ##########################################
            # Open VOC Pascal Annotation             #
            ##########################################
            xml_path = anno_dir + xml_name
            xml_file = open(xml_path, "r")

            # Log
            logger.put(degree='general', msg="Input file : {}".format(xml_path))

            ##########################################
            # Parsing VOC Pascal Annotation          #
            ##########################################
            tree = ET.parse(xml_file)
            root = tree.getroot()

            ##########################################
            # check Image Size tag & Parsing         #
            ##########################################
            size = root.find('size')
            if size == None:
                logger.put(degree='fail', msg="cannot find size tag, size tag is basic information!")
                raise Exception("cannot find size tag, size tag is basic information!")

            xml_width = int(size.find('width').text)
            xml_height = int(size.find('height').text)

            ##########################################
            # Open Image and validate with xml tag   #
            ##########################################
            image_file = str('%s%s%s' % (image_dir, os.path.splitext(xml_name)[0], image_type))

            if not os.path.exists(image_file):
                logger.put(degree='warning', msg="ERROR : [WILL DELETE] does not exist matched image ")
                xml_file.close()
                os.remove(xml_path)
                continue

            image_stream = open(image_file, 'rb')
            img = Image.open(image_stream)
            img_width = int(img.size[0])
            img_height = int(img.size[1])

            # Log
            logger.put(degree='general', msg='Image path : ' + image_file + '\n')
            logger.put(degree='general', msg="xml size (width, height) : " + "(" + str(xml_width) + ',' + str(xml_height) + ")")
            logger.put(degree='general',msg='image size (width, height) : ' + "(" + str(img_width) + ',' + str(img_height) + ")\n")

            if not xml_width == img_width or not xml_height == img_height:
                logger.put(degree='warning',msg="xml and image size different")
                raise Exception("xml and image size different")

            ##########################################
            # Parsing object tag                     #
            ##########################################
            objects = root.findall('object')
            if len(objects) == 0:
                logger.put(degree='warning', msg="ERROR : cannot found object tag")
                continue

            ##########################################
            # Make YOLO label file                   #
            ##########################################
            result_outpath = str(output_dir + xml_name[:-3] + "txt")
            result_outfile = open(result_outpath, "w")

            # Log
            logger.put(degree='general', msg="Output:" + result_outpath + '\n')

            ##########################################
            # Search object contents from annotation #
            ##########################################
            for object in objects:

                cls = object.find('name').text

                ##########################################
                # Validate class candidate               #
                ##########################################
                if cls == None:
                    logger.put(degree='warning', msg="can't find name tag")
                    continue
                elif cls not in classes:
                    logger.put(degree='warning', msg="can't find name tag")
                    continue

                ##########################################
                # Validate box contents                  #
                ##########################################
                bndbox = object.find('bndbox')

                if bndbox == None:
                    logger.put(degree='warning', msg="can't find bndbox tag")
                    raise Exception("can't find bndbox tag")

                xmin = int(float(bndbox.find('xmin').text))
                xmax = int(float(bndbox.find('xmax').text))
                ymin = int(float(bndbox.find('ymin').text))
                ymax = int(float(bndbox.find('ymax').text))

                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convertCoordinate((img_width, img_height), b)

                cls_id = classes.index(cls)

                # Log
                logger.put(degree='general', msg='class name, index : ' + '(' + str(cls) + ", " + str(cls_id) + ')')
                logger.put(degree='general', msg="bndbox Size : " + str(b))
                logger.put(degree='general', msg="convert result : " + str(bb) + '\n')

                ##########################################
                # Write label contents                   #
                ##########################################
                result_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

            ##########################################
            # Close label file & Validation check    #
            ##########################################
            result_outfile.close()

            file_size = os.path.getsize(result_outpath)
            if(file_size == 0):
                logger.put(degree='warning', msg="[WILL DELETE] label file size is 0")
                os.remove(result_outpath)

            ##########################################
            # Write manifest contents                #
            ##########################################
            manifest.writelines('%s\n' % (image_file))
            logger.put(degree='notice', msg="------------------------- Finish XML Parsing -------------------------")

    except Exception as e:
        print(color.BOLD + color.RED + "ERROR : {}".format(e) + color.END)

        if not result_outfile.closed:
            print(color.BOLD + color.RED + "Close result_outfile" + color.END)
            result_outfile.close()
        if os.path.exists(result_outpath):
            print(color.BOLD + color.RED + "delete result outpath" + color.END)
            os.remove(result_outfile)

    ##########################################
    # Close manifest file                    #
    ##########################################
    manifest.close()
    logger.put(degree='notice', msg="------------------------- Finish Convert Annotation -------------------------")
