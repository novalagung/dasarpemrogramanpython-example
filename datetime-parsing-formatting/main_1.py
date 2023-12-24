# A.53.1. Parsing `datetime`

# %% Via `datetime.strptime()` dan kode format

from datetime import datetime

date_string = '1985-04-12 23:20:50'
format_string = '%Y-%m-%d %H:%M:%S'

data_datetime = datetime.strptime(date_string, format_string)
print("datetime:", data_datetime)

date_string = '1985-04-12T23:20:50.52+0700'
format_string = '%Y-%m-%dT%H:%M:%S.%f%z'

data_datetime = datetime.strptime(date_string, format_string)
print("datetime:", data_datetime)

# %% Via `datetime.fromisoformat()` terhadap data ISO Date Time (ISO 8601)

data_datetime = datetime.fromisoformat('1985-04-12T23:20:50.52')
print("datetime:", data_datetime)

data_datetime = datetime.fromisoformat('1985-04-12T23:20:50.52+0700')
print("datetime:", data_datetime)

# %% Via `datetime.fromtimestamp()` terhadap data UNIX Timestamp

data_datetime = datetime.fromtimestamp(1702980333)
print("datetime:", data_datetime)

data_datetime = datetime.fromtimestamp(1702980333.244)
print("datetime:", data_datetime)

from dateutil import tz
data_datetime = datetime.fromtimestamp(1702980333.244, tz=tz.gettz("America/New_York"))
print("datetime:", data_datetime)

# %% Via `dateutil.parser.parse()`

from dateutil import parser

data_datetime = parser.parse("May 12, 2021 8:00 AM")
print("datetime:", data_datetime)
