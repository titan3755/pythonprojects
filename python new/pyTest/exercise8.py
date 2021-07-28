def fizz_buzz(number):
    n1 = int(number)
    if (n1/3).is_integer() and (n1/5).is_integer() == True:
        print('FizzBuzz')
    elif (n1/3).is_integer() == True:
        print('Fizz')
    elif (n1/5).is_integer() == True:
        print('Buzz')
    else:
        print(n1)

var = input('Enter a number: ')
fizz_buzz(var)
