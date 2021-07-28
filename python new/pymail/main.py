import smtplib
import os
email = os.environ.get('EMAILUSERNAME')
password = os.environ.get('EMAILPASS')
print(email, password)
print(os.environ)
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email, password)

    subject = 'Ey wassap... Testing stuff'
    body = 'This shit annoying yet?'
    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email, 'mahmudalmuhaimin123@gmail.com', msg)
