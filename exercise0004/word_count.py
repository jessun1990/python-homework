import re
def count_words(file):
    file = open(file, 'rt')
    file_text = file.read()
    word = re.findall(r'[a-zA-Z0-9]+' ,file_text)
    file.close()
    print(len(word))
    
if __name__ == '__main__':
    count_words("Article.txt")