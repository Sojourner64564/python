import datetime
from math import sin, pi


def bio_rhythm(P, T):
    return sin(2.0 * pi * T / P) * 100


date_entry = input('Введите дату рождения в формате ДД.ММ.ГГГГ ')
year0, month0, day0 = map(int, date_entry.split('.'))
date0 = datetime.date(day0, month0, year0)

date_entry = input('Введите дату расчета в формате ДД.ММ.ГГГГ ')
year, month, day = map(int, date_entry.split('.'))
date = datetime.date(day, month, year)

T = (date - date0).days

print(bio_rhythm(23, T))
print(bio_rhythm(28, T))
print(bio_rhythm(33, T))