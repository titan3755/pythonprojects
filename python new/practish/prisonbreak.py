def invert(x):
    if x == 0:
        return 1
    else:
        return 0


def freed_prisoners(prison):
    main = []
    free_count = 0
    if prison[0] == 0:
        return 0
    else:
        for x in range(len(prison)):
            mapped_list = list(map(invert, prison))
            mapped_list.remove(prison[x - 1])
    return mapped_list


print(freed_prisoners([1, 0, 0, 0, 0, 0, 0]))





