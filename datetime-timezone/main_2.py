# %% A.53.2. Pengenalan timezone (`tz`)

from dateutil import tz
from datetime import date, time, datetime

tzinfo = tz.gettz("America/New_York")

data_time = time(hour=13, minute=14, second=31, tzinfo=tzinfo)
print("time:", data_time)
print("timezone:", data_time.tzinfo)

data_datetime = datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31, tzinfo=tzinfo)
print("datetime:", data_datetime)
print("timezone:", data_datetime.tzinfo)

data_date = date(year=2020, month=1, day=31)
data_time = time(hour=13, minute=14, second=31)
data_datetime = datetime.combine(data_date, data_time, tzinfo=tzinfo)
print("datetime:", data_datetime)
print("timezone:", data_datetime.tzinfo)

# %% ◉ Local vs UTC vs specific timezone

from dateutil import tz
from datetime import date, time, datetime

tzinfo = tz.tzlocal()
data_datetime = datetime(2020, 1, 31, 13, 14, 31, tzinfo=tzinfo)
print("datetime:", data_datetime)

tzinfo = tz.tzutc()
data_datetime = datetime(2020, 1, 31, 13, 14, 31, tzinfo=tzinfo)
print("datetime:", data_datetime)

tzinfo = tz.gettz("America/New_York")
data_datetime = datetime(2020, 1, 31, 13, 14, 31, tzinfo=tzinfo)
print("datetime:", data_datetime)

data_datetime = datetime(2020, 1, 31, 13, 14, 31)
print("datetime:", data_datetime)

# %% ◉ Konversi datetime antar timezone

def print_dt(d):
    print("datetime:", d, "| tz:", d.tzname())

from dateutil import tz
from datetime import date, time, datetime

data = datetime(2020, 1, 31, 13, 14, 31, tzinfo=None)
print_dt(data)

data_local_tz = data.astimezone(tz.tzlocal())
print_dt(data_local_tz)

data_new_york_tz = data.astimezone(tz.gettz("America/New_York"))
print_dt(data_new_york_tz)

data_utc_tz = data.astimezone(tz.tzutc())
print_dt(data_utc_tz)

# %% ◉ Mengubah timezone tanpa konversi datetime

def print_dt(d):
    print("datetime:", d, "| tz:", d.tzname())

from dateutil import tz
from datetime import date, time, datetime

data = datetime(2020, 1, 31, 13, 14, 31, tzinfo=None)
print_dt(data)

data_local_tz = data.replace(tzinfo=tz.tzlocal())
print_dt(data_local_tz)

data_new_york_tz = data.replace(tzinfo=tz.gettz("America/New_York"))
print_dt(data_new_york_tz)

data_utc_tz = data.replace(tzinfo=tz.tzutc())
print_dt(data_utc_tz)
