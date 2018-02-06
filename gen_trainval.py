#coding:utf8

r"""modify xml file in required format no matter where you place your images
Example usage:
    python gen_trainval.py \
        --xmls_dir=/home/user/project/annotations/xmls

Then you can just delete your old xmls folder and use output xmls folder instead
"""

import os
import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string('xmls_dir', '', 'Your own dataset\'s xmls dir inside annotation folder')

FLAGS = flags.FLAGS

def gen_train_val():
    path = FLAGS.xmls_dir
    path_split = os.path.split(path)
    annotation_path = path_split[len(path_split)-1]
    file_list = os.listdir(path)
    fo = open(os.path.join(annotation_path, "trainval.txt"), "w")

    for files in file_list:
        file_name = os.path.splitext(files)[0]
        file_type = os.path.splitext(files)[1]
        if file_type == ".xml":
            fo.write(file_name + "\n")
    
    fo.close()


def main():
    gen_train_val()

if __name__ == "__main__":
    main()