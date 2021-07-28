def factorial(num):
    number = num
    numbers_to_multiply = []
    result = 1
    for x in range(num):
        if num < 0:
            break
        else:
            numbers_to_multiply.append(number)
            number -= 1
    for y in numbers_to_multiply:
        result = result * y
    return result


print(factorial(3))
