# coding: utf-8
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
from random import Random


def generater(random_length, random_num=1):
    activation_code = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    random = Random()
    for i in range(random_num):
        for t in range(random_length):
            activation_code += chars[random.randint(0, len(chars)-1)]
        print(activation_code)
        activation_code = ""

if __name__ == '__main__':
    generater(random_num=200, random_length=20)
