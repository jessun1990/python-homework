# coding: utf-8
# author: jessun
#   date: 2017/6/13 18:56
import os
import codecs


CODE_FILES = ['py']


def get_dir_files(folder_name):
    folder_lists = os.walk(folder_name)
    files_list = []
    for root_name, sub_dirs, root_files in folder_lists:
        for root_file in root_files:
            file = os.path.join(root_name+"/"+root_file)
            files_list.append(file)

    for specific_file in CODE_FILES:
        files_list_processed = [x for x in files_list if x.endswith(specific_file)]
        yield files_list_processed


def parse_code_file(code_file_list):
    comment_line_nums = 1
    code_line_nums = 1
    for code_files in code_file_list:
        for file in code_files:
            with codecs.open(file, 'r', encoding="utf-8") as f:
                for line in f:
                    if line.startswith("\n"):
                        pass
                    elif line.startswith("#"):
                        comment_line_nums = comment_line_nums + 1
                    elif line.startswith('"""'):
                        comment_line_nums = comment_line_nums + 1
                    else:
                        code_line_nums = code_line_nums + 1

    code_info = "该目录下所有代码文件中，代码一共有"
    comment_info = "该目录下所有代码文件中，注释一共有"
    print(code_info+str(code_line_nums)+"行")
    print(comment_info+str(comment_line_nums)+"行")

if __name__ == '__main__':
    # 假定以python文件为例
    project_dir = "projects"

    print("输入的工程目录为 {0} ".format(project_dir))
    parse_code_file(get_dir_files(project_dir))
