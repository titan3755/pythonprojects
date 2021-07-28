import random
import requests
import json

my_words = ['there', 'some', 'water', 'time', 'ability', 'abandon', 'absolute', 'absorb', 'access', 'apple', 'air',
            'axis', 'accept', 'accident', 'actual', 'bat', 'ball', 'bowl', 'bot', 'book', 'boss', 'born', 'border',
            'boot', 'borrow']


def reverse(sentence):
    final_sentence = list(str(sentence)).copy()
    final_sentence.reverse()
    final_str = ''.join(final_sentence)
    return final_str


# def word_jumble():
#     random_word = random.choice(my_words)
#     print(random_word)
#     for x in range(random_word):
#         random_word[]
#     print(jumble)
def get_joke():
    joke = requests.get('https://official-joke-api.appspot.com/jokes/ten').text
    rand_num = random.randint(1, 9)
    dict_json = json.loads(joke)
    main = dict_json[rand_num]['setup']
    punchline = dict_json[rand_num]['punchline']
    return f'{main}\n{punchline}'


print(get_joke())
