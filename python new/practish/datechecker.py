import datetime


def has_friday_13(month, year):
    main_date = datetime.datetime(int(year), int(month), 13)
    if main_date.strftime('%A') == 'Friday':
        return True
    else:
        return False


print(has_friday_13(4, 2020))
