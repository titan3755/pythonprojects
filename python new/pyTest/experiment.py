list_one = [1, 4, 3, 4, 4, 4]
total = 0
var = len(list_one)
for x in range(1, int(var)):
    total = total + list_one[x]

total_corrected = total+1
print('Sum: ', total_corrected)