import time as t
import random as rnd


var = int(input('Enter any integer number: '))
var_test_even = var / 2
var_test_divisibleby4 = var / 4

if var_test_even.is_integer() == True and var_test_divisibleby4.is_integer() == True:
    print('Number is even and divisible by 4')
elif var_test_even.is_integer() == True:
    print('Number is even')
else:
    print('Number is odd')



