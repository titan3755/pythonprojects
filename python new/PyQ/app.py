def register_patient(name, age, is_male, is_old):
    if is_male == 'yes' and is_old == 'no':
        print(name + ' is a new patient and he is ' + age + ' years old')
    elif is_male == 'no' and is_old == 'no':
        print(name + ' is a new patient and she is ' + age + ' years old')
    elif is_male == 'no' and is_old == 'yes':
        print(name + ' is an old patient and she is ' + age + ' years old')
    elif is_male == 'yes' and is_old == 'yes':
        print(name + ' is an old patient and he is ' + age + ' years old')
    else:
        print('Registration Failed!')

def convert_to_secs(value, operator):
    if operator == 'years':
        result = (((int(value) * 365) * 24) * 60) * 60
        print('Years to seconds: ' + str(result) + ' seconds')
    elif operator == 'months':
        result = (((int(value) * 30) * 24) * 60) * 60
        print('Months to seconds: ' + str(result) + ' seconds')
    elif operator == 'hours':
        result = (int(value) * 60) * 60
        print('Hours to seconds: ' + str(result) + ' seconds')