def encrypt(word):
    vowel_replacements = {
        'a': '0',
        'e': '1',
        'i': '2',
        'o': '2',
        'u': '3',
    }
    vowels = ['a', 'e', 'i', 'o', 'u']
    listed = list(word)
    listed.reverse()
    rev = ''.join(listed)
    encrypted_string = ''
    for x in rev:
        if x in vowels:
            encrypted_string += vowel_replacements[x]
        else:
            encrypted_string += x
    encrypted_string += 'aca'
    return encrypted_string


print(encrypt('apple'))

