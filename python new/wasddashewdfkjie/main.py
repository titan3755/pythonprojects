number = input('Enter a number: ')
if number.isnumeric() and int(number) % 2 == 0:
    print('Number is even!')
else:
    print('Number is odd!')
