def int_to_str(num):
    try:
        num = str(num)
        return num
    except Exception:
        return num


def str_to_int(string):
    try:
        string = int(string)
        return string
    except Exception:
        return string


print(type(int_to_str(123)))
print(type(str_to_int('21321')))
