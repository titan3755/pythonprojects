import random as rnd
import time as t
import colorama as cc
import guesses

cc.init()
num_guesses = 3
hint_num = 0
score = 5


def intro():
    print(f"""
    
    {cc.Fore.GREEN}Welcome to Number Guesser Minigame!"""
          +
          f"""
    
    {cc.Fore.CYAN}Try to guess the generated random number between 1 and 9. If you are stuck, use hints.
    But the more hints you use, the lower your score will get. Max number of hints is 2.
    Wrong answers will lower your score too but by a smaller factor.
    Glhf!
    
    {cc.Style.RESET_ALL}
    """

          )


def randomizer():
    ran_int = rnd.randint(1, 9)
    return ran_int


random_num = randomizer()
_intro = intro()
t.sleep(2)
print('Generating Number ...')
t.sleep(1)
print('Number has been generated!')
while num_guesses > 0:
    if random_num == 1:
        response = input('Try to guess the number or type "hint" to get a hint: ')
        if response == '1':
            print(cc.Fore.GREEN + 'You got it right! Score: ' + str(score) + '/5')
            break
        elif response == 'hint':
            if hint_num < 2:
                print(f'Hint: {guesses.hints_1[hint_num]}')
                hint_num += 1
                score -= 1
            else:
                print('Max hints reached!')
        else:
            print('Wrong!')
            num_guesses -= 1
            score -= 1

    elif random_num == 2:
        response = input('Try to guess the number or type "hint" to get a hint: ')
        if response == '2':
            print(cc.Fore.GREEN + 'You got it right! Score: ' + str(score) + '/5')
            break
        elif response == 'hint':
            if hint_num < 2:
                print(f'Hint: {guesses.hints_2[hint_num]}')
                hint_num += 1
                score -= 1
            else:
                print('Max hints reached!')
        else:
            print('Wrong!')
            num_guesses -= 1
            score -= 1
    elif random_num == 3:
        response = input('Try to guess the number or type "hint" to get a hint: ')
        if response == '3':
            print(cc.Fore.GREEN + 'You got it right! Score: ' + str(score) + '/5')
            break
        elif response == 'hint':
            if hint_num < 2:
                print(f'Hint: {guesses.hints_3[hint_num]}')
                hint_num += 1
                score -= 1
            else:
                print('Max hints reached!')
        else:
            print('Wrong!')
            num_guesses -= 1
            score -= 1
    elif random_num == 4:
        response = input('Try to guess the number or type "hint" to get a hint: ')
        if response == '4':
            print(cc.Fore.GREEN + 'You got it right! Score: ' + str(score) + '/5')
            break
        elif response == 'hint':
            if hint_num < 2:
                print(f'Hint: {guesses.hints_4[hint_num]}')
                hint_num += 1
                score -= 1
            else:
                print('Max hints reached!')
        else:
            print('Wrong!')
            num_guesses -= 1
            score -= 1
    elif random_num == 5:
        response = input('Try to guess the number or type "hint" to get a hint: ')
        if response == '5':
            print(cc.Fore.GREEN + 'You got it right! Score: ' + str(score) + '/5')
            break
        elif response == 'hint':
            if hint_num < 2:
                print(f'Hint: {guesses.hints_5[hint_num]}')
                hint_num += 1
                score -= 1
            else:
                print('Max hints reached!')
        else:
            print('Wrong!')
            num_guesses -= 1
            score -= 1
    elif random_num == 6:
        response = input('Try to guess the number or type "hint" to get a hint: ')
        if response == '6':
            print(cc.Fore.GREEN + 'You got it right! Score: ' + str(score) + '/5')
            break
        elif response == 'hint':
            if hint_num < 2:
                print(f'Hint: {guesses.hints_6[hint_num]}')
                hint_num += 1
                score -= 1
            else:
                print('Max hints reached!')
        else:
            print('Wrong!')
            num_guesses -= 1
            score -= 1
    elif random_num == 7:
        response = input('Try to guess the number or type "hint" to get a hint: ')
        if response == '7':
            print(cc.Fore.GREEN + 'You got it right! Score: ' + str(score) + '/5')
            break
        elif response == 'hint':
            if hint_num < 2:
                print(f'Hint: {guesses.hints_7[hint_num]}')
                hint_num += 1
                score -= 1
            else:
                print('Max hints reached!')
        else:
            print('Wrong!')
            num_guesses -= 1
            score -= 1
    elif random_num == 8:
        response = input('Try to guess the number or type "hint" to get a hint: ')
        if response == '8':
            print(cc.Fore.GREEN + 'You got it right! Score: ' + str(score) + '/5')
            break
        elif response == 'hint':
            if hint_num < 2:
                print(f'Hint: {guesses.hints_8[hint_num]}')
                hint_num += 1
                score -= 1
            else:
                print('Max hints reached!')
        else:
            print('Wrong!')
            num_guesses -= 1
            score -= 1
    elif random_num == 9:
        response = input('Try to guess the number or type "hint" to get a hint: ')
        if response == '9':
            print(cc.Fore.GREEN + 'You got it right! Score: ' + str(score) + '/5')
            break
        elif response == 'hint':
            if hint_num < 2:
                print(f'Hint: {guesses.hints_9[hint_num]}')
                hint_num += 1
                score -= 1
            else:
                print('Max hints reached!')
        else:
            print('Wrong!')
            num_guesses -= 1
            score -= 1
if num_guesses <= 0:
    print(cc.Fore.RED + 'You Lost!')
    input('Press enter to close')
else:
    cc.deinit()
    input('Press enter to close')