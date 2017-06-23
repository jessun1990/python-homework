# coding: utf-8
# author: jessun
#   date: 2017/6/15 16:49
# **第 0009 题：**一个HTML文件，找出里面的**链接**。
import re


def html_parse(input_file):
    with open(input_file, 'rt', encoding="utf-8") as f:
        html_content = f.read()
    all_links = re.findall('<a href="(.*?)">', html_content, re.S)
    all_links = [x for x in all_links if not x == '']
    all_links = [x for x in all_links if x.startswith("http")]
    for x in all_links:
        print(x)


if __name__ == '__main__':
    html_parse('index.html')
