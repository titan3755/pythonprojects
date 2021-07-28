def email_slicer(email):
    main_str = str(email)
    if '@' in main_str and main_str.endswith('.com') or main_str.endswith('.ch') or main_str.endswith('.us'):
        if '@gmail.com' in main_str or '@googlemail.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            print(f"""Domain: Google\nUsername: {username}""")
        elif '@yahoo.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            print(f"""Domain: Yahoo\nUsername: {username}""")
        elif '@hotmail.com' in main_str or '@outlook.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            print(f"""Domain: Microsoft\nUsername: {username}""")
        elif '@protonmail.ch' in main_str or '@protonmail.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            print(f"""Domain: ProtonMail\nUsername: {username}""")
        elif '@zoho.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            print(f"""Domain: ZohoMail\nUsername: {username}""")
        elif '@aol.com' in main_str or '@aim.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            print(f"""Domain: AOLMail\nUsername: {username}""")
        elif '@gmx.com' in main_str or '@gmx.us' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            print(f"""Domain: GMXMail\nUsername: {username}""")
        elif '@icloud.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            print(f"""Domain: Apple\nUsername: {username}""")
        elif '@yandex.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            print(f"""Domain: YandexMail\nUsername: {username}""")
        else:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            print(f"""Domain: Custom Domain\nUsername: {username}""")
    elif '@' in main_str:
        username_list = list(main_str)
        username = ''.join(username_list[:username_list.index('@')])
        print(f"""Domain: Unknown\nUsername: {username}""")
    else:
        print('Invalid Email! Must contain domain name')

email_input = input('Enter an email address: ')
email_slicer(email_input)