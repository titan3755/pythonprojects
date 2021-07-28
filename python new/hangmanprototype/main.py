import random
import pyfiglet
import colorama
import time
import math

print(pyfiglet.figlet_format(' H a n g m a n '))
print(f'\nWelcome to Hangman! Try to guess the random word letter by letter.\nYou will have a maximum of three guesses and you will have to guess the word character by character using those three guesses.')

guesses = 3
words = ['apple', 'banana', 'there', 'weed']
random_word = random.choice(words)
listed = list(random_word)
while guesses > 0:
    print(random_word)
    input_letter = input('Enter a letter: ')
    if input_letter in listed:
        listed.remove(input_letter)
        print('Correct letter!')
    else:
        print('Incorrect!')
        guesses -= 1

    if len(listed) == 0:
        print('Game over and you won!')
        break
    else:
        pass
else:
    print('You have run out of guesses!')
    print('You lost!')