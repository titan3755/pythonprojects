count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
    else:
        pass
print(f'We have {count} even numbers')
