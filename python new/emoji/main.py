import random

my_words = ['about', 'what', 'divide', 'accept']
rnd_word = random.choice(my_words)
main = list(rnd_word)
random.shuffle(main)
final_word = ''.join(main)
print(final_word)