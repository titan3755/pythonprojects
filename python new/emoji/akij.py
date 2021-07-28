class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('Talking')


person1 = Person('Mofiz Bhai')
print(person1.name)
person1.talk()
