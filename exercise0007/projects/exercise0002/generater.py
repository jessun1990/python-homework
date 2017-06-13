from random import Random


def generater(random_length, random_num=1):
    activation_code = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    random = Random()
    for i in range(random_num):
        for t in range(random_length):
            activation_code += chars[random.randint(0, len(chars)-1)]
        return(activation_code)
        activation_code = ""

if __name__ == '__main__':
    generater(random_length=20)
