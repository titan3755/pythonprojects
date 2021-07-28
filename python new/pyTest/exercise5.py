num_list = range(1, 500)
var = int(input('Enter a number: '))
var3 = 0

for x in num_list:
    var2 = var/x
    if var2.is_integer() == True:
        var3 = var3 + 1
        print('Divisor ' + str(var3) + ' for ' + str(var) + ' is ' + str(var2))

print(str(var3) + ' Total divisors for ' + str(var))

