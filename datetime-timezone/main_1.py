# %% A.53.1. Pengenalan `date`, `time`, dan `datetime`

from datetime import date, time, datetime

data_date = date(year=2020, month=1, day=31)
print("date:", data_date)
print(" ➜ year:", data_date.year)
print(" ➜ month:", data_date.month)
print(" ➜ day:", data_date.day)

data_time = time(hour=13, minute=14, second=31)
print("time:", data_time)
print(" ➜ hour:", data_time.hour)
print(" ➜ minute:", data_time.minute)
print(" ➜ second:", data_time.second)
print(" ➜ timezone:", data_time.tzinfo)

data_datetime = datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31)
print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)

# %% ◉ Combining `date` & `time`

data_datetime = datetime.combine(data_date, data_time)
print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)

# %% Mengambil datetime hari ini / sekarang

data1 = datetime.now()
print("sekarang (datetime):", data1)

data2 = datetime.today()
print("sekarang (datetime):", data2)

data2 = date.today()
print("sekarang (date):", data2)
