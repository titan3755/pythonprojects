import random

class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def decelerate(self):
        self.speed -= 5

    def rnd_acc(self):
        self.speed += random.randint(1, 30)

    def rnd_dcc(self):
        if self.speed > 5:
            self.speed -= random.randint(1, 30)
        elif self.speed < 0:
            pass
        else:
            return None

car1 = Car('RollsRoyce')
while True:
    inputted_value = input('> ')
    if inputted_value == 'acc':
        car1.accelerate()
        print(car1.speed)
    elif inputted_value == 'dcc':
        car1.decelerate()
        print(car1.speed)
    elif inputted_value == 'racc':
        car1.rnd_acc()
        print(car1.speed)
    elif inputted_value == 'rdcc':
        car1.rnd_dcc()
        print(car1.speed)
    else:
        print('Invalid Command!')