from const import *


def get_birthdays_per_week(users):
    week = {
        '1': 'Monday',
        '2': 'Tuesday',
        '3': 'Wednesday',
        '4': 'Thursday',
        '5': 'Friday',
        '6': 'Monday',
        '7': 'Monday',
    }

    week_days = {'Monday': '',
                 'Tuesday': '',
                 'Wednesday': '',
                 'Thursday': '',
                 'Friday': '',
                 }

    today = str(datetime.datetime.isoweekday(datetime.datetime.now()))
    first = dct_fist[today].date()
    last = dct_last[today].date()

    for i in users:
        for key, value in i.items():
            if int(str(value).split('-')[0]) < current_year:
                value = datetime.date(year=current_year, month=value.month, day=value.day)
                if int(str(value).split('-')[1]) in (first.month, last.month):
                    if first <= value <= last:
                        week_days[week[str(datetime.date.isoweekday(value))]] += key + ', '

    for key, value in week_days.items():
        if value != '':
            value = value[:-2]
            week_days[key] = value
            print(key + ':', value)


get_birthdays_per_week(
    [{'Misha': datetime.date(2000, 8, 20)}, {'Artem': datetime.date(2000, 8, 20)}, {'Dima': datetime.date(2000, 9, 2)},
     {'Grisha': datetime.date(2001, 8, 26)}])
