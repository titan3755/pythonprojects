import random

def rps(response):
    list_rps = ['rock', 'paper', 'scissors']
    choice = random.choice(list_rps)
    if response == 'rock' and choice == 'rock':
        return f"You chose rock and I also chose rock...\nIt's a Draw!"
    elif response == 'rock' and choice == 'paper':
        return f"You chose rock and I chose paper...\nYou lost!"
    elif response == 'rock' and choice == 'scissors':
        return f"You chose rock and I chose scissors...\nYou won!"
    elif response == 'paper' and choice == 'rock':
        return f"You chose paper and I chose rock...\nYou won!"
    elif response == 'paper' and choice == 'paper':
        return f"You chose paper and I also chose paper...\nIt's a Draw!"
    elif response == 'paper' and choice == 'scissors':
        return f"You chose paper and I chose rock...\nYou lost!"
    elif response == 'scissors' and choice == 'rock':
        return f"You chose scissors and I chose rock...\nYou lost!"
    elif response == 'scissors' and choice == 'paper':
        return f"You chose scissors and I chose paper...\nYou won!"
    elif response == 'scissors' and choice == 'scissors':
        return f"You chose scissors and I also chose scissors...\nIt's a Draw!"

print(rps())