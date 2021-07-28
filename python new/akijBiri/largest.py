numbers = [1, 2, 10, 500, 100, 1, 75, 34, 20, 25]
def largest(num_list):
    largest_num = numbers[0]
    for x in range(len(num_list)):
        if numbers[x] > largest_num:
            largest_num = numbers[x]
        else:
            pass
    print(largest_num)
largest(numbers)