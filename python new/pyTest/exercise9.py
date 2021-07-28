def multiples(limit):
    for x in range(1, int(limit)):
        if (x/3).is_integer() or (x/5).is_integer() == True:
            return x

total = 0
var1 = input('Enter a number as limit: ')
list1 = [multiples(var1)]
length = len(list1)
for i in range(1, int(length)):
    total = total + list1[i]





print('Sum: ' + str(total))


