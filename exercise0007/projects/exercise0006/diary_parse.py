# coding: utf-8
# author: jessun
#   date: 2017/6/12 22:30
# **第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
from collections import Counter
import codecs
import glob
import os
import re


# 需要忽略的词汇
unimportant_words = ['I', 'the', 'of', 'to', 'and', 'a', 'be', 'in', 'that', 'for', 'with',
                     'will', 'is', 'from', 'by', 'as', 'it', 'not']


def get_diary_list(folder_name):
    # 将目录下的txt文件返回为地址列表
    url = os.path.join(folder_name+"/*.txt")
    diary_files = glob.glob(str(url))
    return list(diary_files)


def diary_parse(diarys_list):
    try:
        for diary in diarys_list:
            with codecs.open(diary, 'r', encoding="utf-8") as f:
                diary_text = f.read()
                reg_word = re.findall(r'[a-zA-Z0-9]+', diary_text)
            reg_word = [i for i in reg_word if i not in unimportant_words]
            counts = Counter(reg_word)

            diary_filename = str(diary).split('/')[-1]
            print("日记 "+str(diary_filename)+" 中最重要的词")
            print('{:>9} | {:}'.format("单词", "出现次数"))
            for diary_word, word_count in counts.most_common(3):
                output_line = '{:>10} | {:<10}'.format(diary_word, word_count)
                print(output_line)
            print("\n")

    except Exception as e:
        print("程序出现异常")

if __name__ == '__main__':
    diary_parse(get_diary_list("diarys"))
