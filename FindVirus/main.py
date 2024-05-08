import os
import time
import sys
from datetime import datetime


TIMES_BORDER = 86400        # 1 день
CHECK_DIRECTORY = r"/home/qwerty/PycharmProjects/Python_life_hacks"
FILE_LOG = r"/home/qwerty/PycharmProjects/Python_life_hacks/FindVirus/log.txt"
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'


def clear_log():
    f = open(FILE_LOG, "w")
    f.close()


def virus_find(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            file = os.path.join(root, name)
            if check(file):
                add_to_log(file)


def check(file):
    current_ts = time.time()
    change_time = get_change_time(file)
    return current_ts - change_time < TIMES_BORDER


def get_change_time(file):
    m_time = os.stat(file).st_mtime     # Время последней модификации
    a_time = os.stat(file).st_atime     # Время последнего доступа.
    c_time = os.stat(file).st_ctime     # время создания
    return max(m_time, a_time, c_time)


def add_to_log(file):
    """
    datetime.fromtimestamp(timestamp, tz=None)
    Возвращает локальную дату и время, соответствующие временной метке POSIX, такой, как возвращается функцией time.time().
    Переводит 1715088631.561204 в 2024-05-07 16:30:31.561204
    """
    adding_string = file + ": " + datetime.fromtimestamp(get_change_time(file)).strftime(DATE_FORMAT) + "\n"
    f = open(FILE_LOG, "a")
    f.write(adding_string)
    f.close()


if __name__ == '__main__':
    clear_log()
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        virus_find(directory)
    else:
        virus_find(CHECK_DIRECTORY)
