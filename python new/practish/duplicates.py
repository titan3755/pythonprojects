import time

start = time.time()


def single_number(nums):
    result = 0
    for x in nums:
        if nums.count(x) == 1:
            result = x
    return result



time.sleep(0.5)

print(single_number([0, 1, 0, 1, 0, 1, 99]))

end = time.time()
print(end - start - 0.5)
