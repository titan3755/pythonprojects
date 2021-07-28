def get_num_type(limit):
    for x in range(1, int(limit) + 1):
        type_checker = x/2
        if type_checker.is_integer() == True:
            print(str(x) + ' IS EVEN')
        else:
            print(str(x) + ' IS ODD')

var = input('Enter any number: ')
get_num_type(var)