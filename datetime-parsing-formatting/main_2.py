# A.54.2. Formatting `datetime`

# %% ◉ Method `datetime.strftime()` dan kode format

from datetime import datetime

data_datetime = datetime.fromtimestamp(1702980333, tz=None)
print(data_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f%z'))

data_datetime = datetime.fromisoformat('1985-04-12T23:20:50.52+0700')
print(data_datetime.strftime('%m/%d/%Y %H:%M:%S %z'))

# %% ◉ Method `datetime.isoformat()` ➜ ISO Date Time (ISO 8601)

data_datetime = datetime.now()
print(data_datetime.isoformat())

# %% ◉ Method `datetime.timestamp()` ➜ UNIX timestamp

data_datetime = datetime.now()
print(data_datetime.timestamp())
