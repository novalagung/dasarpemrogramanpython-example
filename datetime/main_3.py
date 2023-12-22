
# %% basic parsing

from datetime import datetime

date_string = '1985-04-12 23:20:50'
format_string = '%Y-%m-%d %H:%M:%S'

data_datetime = datetime.strptime(date_string, format_string)
print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)

date_string = '1985-04-12T23:20:50.52+0700'
format_string = '%Y-%m-%dT%H:%M:%S.%f%z'

data_datetime = datetime.strptime(date_string, format_string)
print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)

# %% from iso format

data_datetime = datetime.fromisoformat('1985-04-12T23:20:50.52')
print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)

data_datetime = datetime.fromisoformat('1985-04-12T23:20:50.52+0700')
print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)

# %% from timestamp

data_datetime = datetime.fromtimestamp(1702980333, tz=None)
# data_datetime = datetime.fromtimestamp(1702980333.223, tz=None)
print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)

# %% parser

from dateutil import parser
from datetime import datetime

data_datetime = parser.parse("May 12, 2021 8:00 AM")
print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)
