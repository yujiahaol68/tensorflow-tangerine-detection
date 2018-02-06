#coding:utf8

r"""change sample image and xml annotation files into {label}_{index}.jpg, {label}_{index}.xml format
Example usage:
    python clean_data.py \
        --data_dir=/home/user/project \
        --label=tangerine

WARNING: Dir annotations should be right in the project. And both .xml and .jpg files should be in annotations dir.
"""

import os
import tensorflow as tf
import shutil

flags = tf.app.flags
flags.DEFINE_string('data_dir', '', 'Root directory to your own dataset.')
flags.DEFINE_string('label', '', 'A label that will be used to detect.')

FLAGS = flags.FLAGS

def rename():
    path = os.path.join(FLAGS.data_dir, "annotations") 
    file_list = os.listdir(path)
    start_index = 1

    for files in file_list:
        new_name = FLAGS.label + "_" + str(start_index)
        file_name = os.path.splitext(files)[0]
        filetype = os.path.splitext(files)[1]
        if filetype == ".xml":
            continue

        old_img_dir = os.path.join(path, files)
        new_img_dir = os.path.join(path, new_name + filetype)

        for f in file_list:
            f_name = os.path.splitext(f)[0]
            f_type = os.path.splitext(f)[1]
            if f_type == ".jpg":
                continue

            old_xml_dir = os.path.join(path, f)
            new_xml_dir = os.path.join(path, new_name + f_type)

            if f_name == file_name:
                os.rename(old_img_dir, new_img_dir)
                os.rename(old_xml_dir, new_xml_dir)
                start_index = start_index + 1
                break

def move_files():
    new_image_path = os.path.join(FLAGS.data_dir, "images")
    new_xml_path = os.path.join(FLAGS.data_dir, "annotations")
    new_xml_path = os.path.join(new_xml_path, "xmls")
    os.mkdir(new_image_path)
    os.mkdir(new_xml_path)
    old_data_dir = os.path.join(FLAGS.data_dir, "annotations")
    file_list = os.listdir(old_data_dir)
    for f in file_list:
        f_type = os.path.splitext(f)[1]
        if f_type == ".jpg":
            shutil.move(os.path.join(old_data_dir, f), os.path.join(new_image_path, f))
        else:
            shutil.move(os.path.join(old_data_dir, f), os.path.join(new_xml_path, f))

def main():
    rename()
    move_files()

if __name__ == "__main__":
    main()