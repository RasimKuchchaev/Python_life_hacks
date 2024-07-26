# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import smtplib
from email.mime.text import MIMEText

SERVER = 'smtp.yandex.ru'
PORT = 587
LOGIN = 'tt3stt3st123'
PASSWORD = 'afsdjflasdfjlsadfjasdlfasjdlf'
FROM_EMAIL = 'tt3stt3st123@yandex.ru'
TEXT_TYPE = 'plain' # html


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
    send_email('tt3st1test1@yandex.ru', 'Тема письма', 'Тело письма')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
