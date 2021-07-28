list_numbers = [1, 1, 2, 6, 4, 9, 20, 8, 3, 6, 20, 3, 4, 1, 2, 1, 2]
uniques = []
for x in list_numbers:
    if x not in uniques:
        uniques.append(x)
print(uniques)