import math

input_first = float(input('Enter a number: '))
input_second = float(input('Enter another number: '))

result = input_first * input_second
if result <= 1000:
    print(result)
elif result > 1000:
    print(input_first + input_second)
else:
    print('Invalid')
