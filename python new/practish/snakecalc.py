def snakefill(n):
    total_spaces = n*n
    power = 1
    times_eaten = 0
    while True:
        if 2**power < total_spaces:
            power += 1
            times_eaten += 1
        else:
            break
    return times_eaten


print(snakefill(7))