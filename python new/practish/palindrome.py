# def palindrome_checker(num):
#     listed = list(str(num))
#     for x in listed:
#         int(x)
#     listed_reverse = list(str(num))
#     listed_reverse.reverse()
#     if listed == listed_reverse:
#         return True
#     else:
#         return False
def pal_seq(n):
    steps = 0
    listed_reverse = list(str(n))
    listed_reverse.reverse()
    main_reversed_list = int(''.join(listed_reverse))
    return main_reversed_list


