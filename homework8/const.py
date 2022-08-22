import datetime
from calendar import monthrange

current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
days_in_month = monthrange(current_year, current_month)[1]
days_in_last_month = monthrange(current_year, current_month - 1)[1]

dct_fist = {
    '1': datetime.datetime.now() - datetime.timedelta(days=2),
    '2': datetime.datetime.now() - datetime.timedelta(days=3),
    '3': datetime.datetime.now() - datetime.timedelta(days=4),
    '4': datetime.datetime.now() - datetime.timedelta(days=5),
    '5': datetime.datetime.now() - datetime.timedelta(days=6),
    '6': int(datetime.datetime.now().day),
    '7': datetime.datetime.now() - datetime.timedelta(days=1),
}

dct_last = {
    '1': datetime.datetime.now() + datetime.timedelta(days=4),
    '2': datetime.datetime.now() + datetime.timedelta(days=3),
    '3': datetime.datetime.now() + datetime.timedelta(days=2),
    '4': datetime.datetime.now() + datetime.timedelta(days=1),
    '5': int(datetime.datetime.now().day),
    '6': datetime.datetime.now() + datetime.timedelta(days=6),
    '7': datetime.datetime.now() + datetime.timedelta(days=5),
}
