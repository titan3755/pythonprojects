import time as t


time = t.localtime()
current_year = time.tm_year

var1 = input('Enter your name: ')
var2 = int(input('Enter your age: '))

var2 = (100 - var2) + current_year

print(var1 + ', You will be 100 years old in ' + str(var2) + ' AD')

var3 = input('Enter anything: ')
var4 = input('Enter a number: ')

print('Repeating...')
t.sleep(2)
for x in range(int(var4)):
    print(var3)



