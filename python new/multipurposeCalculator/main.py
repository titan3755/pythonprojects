numbers_input = input('Enter your numbers here and separate them by a comma: ')
main_numbers = numbers_input.strip().replace(' ', '').split(',')
operator = []
num = 0
num2 = -1
result = ''
if len(main_numbers) < 2:
    print('Numbers cannot be less than 2 values!')
else:
    for x in range(len(main_numbers) - 1):
        op = input(f'Enter operator after {main_numbers[num]}: ')
        if op == '+' or op == '-' or op == '*' or op == '/':
            operator.append(op)
            num = num + 1
        else:
            print('Invalid operator!')
            break

    for x in range(len(operator)):
        num2 += 1
        result += main_numbers[num2] + operator[num2]

    print('Result: ' + eval(result + main_numbers[-1]))