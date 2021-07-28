import random

list_everything = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
                   '%', '^', '&', '*', '(', ')']
cin = input('Enter password length: ')



def password_randomizer(length):
    output = ''
    for x in range(length):
        output += random.choice(list_everything)
    print(f'Generated Password: {output}')


if cin.isnumeric():
    password_randomizer(int(cin))
else:
    print('Input Invalid!')
