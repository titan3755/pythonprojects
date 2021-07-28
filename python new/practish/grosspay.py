hours = input('Hours? ')
rate = input('Rate of pay? ')
try:
    result = float(hours)*float(rate)
    print(f'The gross pay is: {result}')
except Exception:
    print('Error!')
