# coding:utf-8
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
from PIL import Image, ImageDraw, ImageFont


def add_num_to_image(input_image, add_num, output_image):
    input_img = Image.open(input_image)
    im_width, im_height = input_img.size

    font_width = im_width/10
    font_height = im_height/10
    font_size = im_width/11

    x = im_width/7*6
    y = im_height/100

    add_position = (x, y)
    add_text_font = ImageFont.truetype(font="font.ttf", size=int(font_size))
    add_color = (255, 0, 0)

    draw = ImageDraw.Draw(input_img)
    draw.text(add_position, add_num, add_color, add_text_font)
    input_img.show()
    input_img.save(output_image)

if __name__ == '__main__':
    add_num_to_image('origin.jpeg', "+1", "output.png")
