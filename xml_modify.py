#coding:utf8

r"""modify xml file in required format no matter where you place your images
Example usage:
    python xml_modify.py \
        --xmls_dir=/home/user/project/annotations/xmls \
        --image_dir=/home/user/project/images \
        --output_dir=/home/user/project/xmls

Then you can just delete your old xmls folder and use output xmls folder instead
"""

import os
from xml.etree import ElementTree
import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string('xmls_dir', '', 'xmls dir that inside annotations dir. inside should have all your .xml annotaions file')
flags.DEFINE_string('image_dir', '', 'images directory of your own dataset. inside should have all your jpg files')
flags.DEFINE_string('output_dir', '', 'new XML files Output directory')

FLAGS = flags.FLAGS

def main():
    folder = FLAGS.image_dir
    folder_split = os.path.split(folder)
    folder_text = folder_split[len(folder_split)-1]

    path = FLAGS.xmls_dir
    output_path = FLAGS.output_dir

    file_list = os.listdir(path)
    for file in file_list:
        file_name = os.path.splitext(file)[0]
        document = ElementTree.ElementTree(file=os.path.join(path, file))
        document.find("path").text = os.path.join(folder, file_name + ".jpg")
        document.find("folder").text = folder_text
        document.find("filename").text = file_name + ".jpg"
        print("processing " + file)

        document.write(os.path.join(output_path, file), encoding='utf-8', xml_declaration=False)

if __name__ == "__main__":
    main()