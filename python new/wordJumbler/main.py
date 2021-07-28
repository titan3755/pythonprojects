import random

list_of_words = ['add', 'about', 'dwell', 'accent', 'hand']
correct = random.choice(list_of_words)
guesses = 2


def word_jumble():
    output_main = []
    output = []
    ultimate_output = ''
    random_word = correct
    word_length = len(random_word)
    for x in range(word_length):
        if x not in list_of_words:
            output.append(x)
        else:
            pass
    random.shuffle(output)
    for y in output:
        output_main.append(output[y])
    for z in output_main:
        ultimate_output += random_word[z]

    if ultimate_output == correct:
        return None
    elif ultimate_output != correct:
        return ultimate_output


main_word = word_jumble()

while True:
    word = input(f'Your word is {main_word}\n\nGuess the correct word: ')
    if word == correct and guesses > 0:
        print(f'You have guessed the correct word! correct word was indeed {correct}')
        break
    elif word != correct and guesses > 0:
        guesses -= 1
        print(f'You got it wrong! Try again...')
    elif word != correct and guesses <= 0:
        print('You lost!')
        break

