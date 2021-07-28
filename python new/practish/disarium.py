def is_disarium(n):
    list_str = list(str(n))
    list_nums = []
    sum = 0
    for num in list_str:
        list_nums.append(int(num))
    for x in list_nums:
        index = list_nums.index(x)
        sum += x**(index + 1)
    if sum == n:
        return True
    else:
        return False


print(is_disarium(518))