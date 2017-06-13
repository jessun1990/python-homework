# coding: utf-8
# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
import re
import codecs


def count_words(file):
    with codecs.open(file, 'r', encoding="utf-8") as f:
        file_text = f.read()
        word = re.findall(r'[a-zA-Z0-9]+', file_text)
    print(str(file) + "单词的个数为" + str(len(word)))
    
if __name__ == '__main__':
    count_words("Article.txt")
