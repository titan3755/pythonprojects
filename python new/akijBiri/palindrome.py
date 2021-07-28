print('Enter 5 words and the palindromes will be returned.')

in_1 = input('Enter word: ')
in_2 = input('Enter word: ')
in_3 = input('Enter word: ')
in_4 = input('Enter word: ')
in_5 = input('Enter word: ')

def find_palindrome(word):
    output = list(str(word).replace(' ', ''))
    revCopy = output.copy()
    revCopy.reverse()
    output_joined = ''.join(output)
    rev_joined = ''.join(revCopy)
    if output_joined.isnumeric() is False:
        if output_joined == rev_joined:
            print(f'{word} is a palindrome\n')
        else:
            print(f'{word} is not a palindrome\n')
    else:
        print('Invalid')
find_palindrome(in_1)
find_palindrome(in_2)
find_palindrome(in_3)
find_palindrome(in_4)
find_palindrome(in_5)
