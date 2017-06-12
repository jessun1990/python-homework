# coding: utf-8
# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
import re


def count_words(file):
    file = open(file, 'rt')
    file_text = file.read()
    word = re.findall(r'[a-zA-Z0-9]+' ,file_text)
    file.close()
    print(len(word))
    
if __name__ == '__main__':
    count_words("Article.txt")