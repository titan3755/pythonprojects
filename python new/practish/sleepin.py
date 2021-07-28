def sleep_in(weekday, vacation):
    if weekday is True and vacation is False:
        return False
    elif weekday is True and vacation is True:
        return True
    elif weekday is False and vacation is True:
        return True
    elif weekday is False and vacation is False:
        return True
    else:
        return None

print(sleep_in(False, False))
