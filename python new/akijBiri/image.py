
while True:
    input_ = input('Enter a number: ')
    if input_.isnumeric():
        if int(input_) % 2 == 0:
            print(f'{input_} is an even number.')
        else:
            print(f'{input_} is an odd number.')
    else:
        print(f'{input_} is not a number!')
