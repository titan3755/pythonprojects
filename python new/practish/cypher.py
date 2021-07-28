import string

def atbash(txt):
    listed = list(txt)
    listed_alphabets = list(string.ascii_lowercase)
    listed_upper = list(string.ascii_uppercase)
    listed_alphabets_rev = list(string.ascii_lowercase)
    listed_alphabets_rev.reverse()
    listed_upper_rev = list(string.ascii_uppercase)
    listed_upper_rev.reverse()

    encrypted_sentence = ''

    for letter in listed:
        if letter.islower():
            index = listed_alphabets.index(letter)
            encrypted_sentence += listed_alphabets_rev[index]
        elif letter.isupper():
            index = listed_upper.index(letter)
            encrypted_sentence += listed_upper_rev[index]
        else:
            encrypted_sentence += letter

    return encrypted_sentence


print(atbash('Christmas is the 25th of December'))



