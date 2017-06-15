# coding: utf-8
# author: jessun
#   date: 2017/6/15 15:59
# **第 0008 题：**一个HTML文件，找出里面的**正文**。
import re


def html_parse(input_file):
    with open(input_file, 'rt', encoding='utf-8') as f:
        html_content = f.read()

    html_body = re.search(r'<body>(.*)</body>', html_content, re.S)
    print(input_file+'的正文内容为')
    print(html_body.group(1))


if __name__ == '__main__':
    html_parse("index.html")
