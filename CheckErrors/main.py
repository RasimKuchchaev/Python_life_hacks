# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import smtplib
from email.mime.text import MIMEText

FILE = 'error.log'
SERVER = 'smtp.yandex.ru'
PORT = 587
LOGIN = 'tt3stt3st123'
PASSWORD = 'afsdjflasdfjlsadfjasdlfasjdlf'

TO = 'tt3st1test1@yandex.ru'
FROM_EMAIL = 'tt3stt3st123@yandex.ru'
TEXT_TYPE = 'html'


def check_errors(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    notices = 0
    warnings = 0
    errors = 0
    for line in lines:
        if '[php7:notice]' in line:
            notices += 1
        elif '[php7:warn]' in line:
            warnings += 1
        elif '[php7:error]' in line:
            errors += 1
    if notices or warnings or errors:
        send_report(notices, warnings, errors)


def send_report(notices, warnings, errors):
    message = '<div>Типы ошибок и их количество:<br />'
    message += '<b>Notices:</b> ' + str(notices) + '<br />'
    message += '<b>Warnings:</b> ' + str(warnings) + '<br />'
    message += '<b>Errors:</b> ' + str(errors) + '</div>'
    send_email(TO, 'Есть ошибки в логах', message)


def send_email(to, subject, message):
    msg = MIMEText(message, TEXT_TYPE, 'utf-8')
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to

    smtp = smtplib.SMTP(SERVER, PORT)
    smtp.starttls()
    smtp.login(LOGIN, PASSWORD)
    smtp.send_message(msg)
    smtp.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_errors(FILE)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
