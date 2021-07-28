num_dict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

c_in = input('Enter Phone: ')
list_words = []
for x in c_in:
    list_words.append(num_dict[x])
final = ' '.join(list_words)
print(final)