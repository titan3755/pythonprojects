import math


def weight(r, h):
    volume_cc = math.pi * int(r) ** 2 * int(h)
    mass = (volume_cc * 1) / 1000
    return round(mass, 2)


print(weight(15, 10))
