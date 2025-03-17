"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    from datetime import datetime, timedelta
    dt_now=datetime.now()
    delta=timedelta(days=1)
    yes=dt_now-delta
    tom=dt_now+delta
    delta2=timedelta(days=30)
    mon=dt_now+delta2
print(yes,tom,mon)
 


def str_2_datetime(date_string):
    string="01/01/20 12:10:03.234567"
    datetime.strptime(string, '%d/%m/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
