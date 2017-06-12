# coding: utf-8
# **第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import glob
import os
from PIL import Image


def convert_images(input_folder, output_folder, size):
    url = os.path.join(input_folder+"/*.jpg")
    images = glob.glob(str(url))
    for image in images:
        file_name, ext_name = os.path.splitext(image)
        file_name2 = os.path.split(file_name)
        im = Image.open(image)
        im.thumbnail(size)
        if not os.path.isdir(output_folder):
            os.mkdir(output_folder)
        im.save(output_folder+r"/"+file_name2[1]+ext_name)
    print(u"图片转换完成")

if __name__ == '__main__':
    image_size = [100, 300]
#     convert_images(image_size)
    convert_images("input", "output", image_size)
