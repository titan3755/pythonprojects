from plyer import notification
import time as t
import datetime



def notify(ttl, msg):
    notify_me = notification.notify(title=ttl, message=msg, app_icon=None, timeout=10)
    return notify_me

while True:
    x = datetime.datetime.now()
    if x.hour == 4 and x.minute == 50:
        notify('Fazr Prayer', 'Its time for Fazr prayer!')
        t.sleep(61)
    elif x.hour == 14 and x.minute == 0:
        notify('Zuhr prayer', 'Its time for Zuhr prayer!')
        t.sleep(61)
    elif x.hour == 17 and x.minute == 0:
        notify('Asr prayer', 'Its time for Asr prayer!')
        t.sleep(61)
    elif x.hour == 18 and x.minute == 50:
        notify('Maghrib prayer', 'Its time for Maghrib prayer!')
        t.sleep(61)
    elif x.hour == 20 and x.minute == 30:
        notify('Isha prayer', 'Its time for Isha prayer!')
    else:
        pass
