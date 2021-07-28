range_f = input('Enter range: ')
previous_number = 1
previous_number_2 = 1
current_number = 1
main = 0
result = [0, 1, 1]
if range_f.isdigit():
    for x in range(int(range_f)):
        current_number = previous_number_2 + current_number
        result.append(current_number)
        previous_number_2 = current_number - previous_number_2
    print(f'Fibonacci Sequence: {str(result).replace("[", "").replace("]", "")}')
    for x in result:
        main += x
    print(f'Sum: {main}')
else:
    print('Range is not integer!')
