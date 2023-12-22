# %% basic timezone

from dateutil import tz
from datetime import date, time, datetime

tzinfo = tz.gettz("America/New_York")

data_time = time(hour=13, minute=14, second=31, tzinfo=tzinfo)
print("time:", data_time)
print(" ➜ hour:", data_time.hour)
print(" ➜ minute:", data_time.minute)
print(" ➜ second:", data_time.second)
print(" ➜ timezone:", data_time.tzinfo)

data_datetime = datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31, tzinfo=tzinfo)
print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)

data_date = date(year=2020, month=1, day=31)
data_time = time(hour=13, minute=14, second=31)
data_datetime = datetime.combine(data_date, data_time, tzinfo=tzinfo)
print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)

# %%

from dateutil import tz
from datetime import date, time, datetime

data_datetime = datetime(2020, 1, 31, 13, 14, 31, tzinfo=None)
print("datetime:", data_datetime)

tzinfo = tz.tzlocal()
data_datetime = datetime(2020, 1, 31, 13, 14, 31, tzinfo=tzinfo)
print("datetime:", data_datetime)

tzinfo = tz.gettz("America/New_York")
data_datetime = datetime(2020, 1, 31, 13, 14, 31, tzinfo=tzinfo)
print("datetime:", data_datetime)

tzinfo = tz.tzutc()
data_datetime = datetime(2020, 1, 31, 13, 14, 31, tzinfo=tzinfo)
print("datetime:", data_datetime)

# %%

def print_dt(str, d):
    print(str)
    print(" ➜ datetime:", d)
    print(" ➜ timezone:", d.tzname())

from dateutil import tz
from datetime import date, time, datetime

data_dt = datetime(2020, 1, 31, 13, 14, 31, tzinfo=None)
print_dt("data_dt in default tz", data_dt)

data_dt_local_tz = data_dt.astimezone(tz.tzlocal())
print_dt("data_dt in local tz", data_dt_local_tz)

data_dt_new_york_tz = data_dt.astimezone(tz.gettz("America/New_York"))
print_dt("data_dt in New York tz", data_dt_new_york_tz)

data_dt_utc_tz = data_dt.astimezone(tz.tzutc())
print_dt("data_dt in UTC tz", data_dt_utc_tz)

# %%

data_dt_local_tz = data_dt.replace(tzinfo=tz.tzlocal())
print_dt("data_dt in local tz", data_dt_local_tz)

data_dt_new_york_tz = data_dt.replace(tzinfo=tz.gettz("America/New_York"))
print_dt("data_dt in New York tz", data_dt_new_york_tz)

data_dt_utc_tz = data_dt.replace(tzinfo=tz.tzutc())
print_dt("data_dt in UTC tz", data_dt_utc_tz)

# %%
