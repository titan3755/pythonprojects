import string


def to_boolean_list(word):
    letters = list(string.ascii_lowercase)
    letters.insert(0, '0')
    listed_word = list(word.lower())
    bitstring = ''
    boolean_list = []
    for letter in listed_word:
        index = letters.index(letter)
        if index % 2 == 0:
            bitstring += '0'
        else:
            bitstring += '1'
    for bit in bitstring:
        if bit == '1':
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    return boolean_list


print(to_boolean_list('tesh'))





