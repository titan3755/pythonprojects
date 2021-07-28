import colorama
import random
import proj

response_from = input('Convert From[type kg, lbs, oz or ton]: ')
response_to = input('Convert To[type kg, lbs, oz or ton]: ')
response_from = response_from.lower()
response_to = response_to.lower()
value = input(f'___ {response_from} to {response_to} ? ')
if response_from == 'kg' or response_from == 'lbs' or response_from == 'oz' or response_from == 'ton' and response_to == 'kg' or response_to == 'lbs' or response_to == 'oz' or response_to == 'ton' and value.isnumeric() is True:
    print('The result is: ' + str(proj.convert(response_from.lower(), response_to.lower(), float(value))) + ' ' + response_to.lower())
else:
    print('Invalid Values!')