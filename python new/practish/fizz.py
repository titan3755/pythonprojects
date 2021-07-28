def fizz_buzz(user_input):
    if int(user_input) % 3 == 0 and int(user_input) % 5 == 0:
        print('FizzBuzz')
    elif int(user_input) % 3 == 0:
        print('Fizz')
    elif int(user_input) % 5 == 0:
        print('Buzz')
    else:
        print(user_input)


main_input = input('Enter an integer number: ')
fizz_buzz(main_input)
