amount_one = 1000000
amount_two = 0.01

if (amount_one * (2**30)) > (amount_two * (2**30)):
    print(f'Amount one is greater than amount two')

else:
    print(f'Amount two is greater than amount one')