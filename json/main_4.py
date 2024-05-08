# A.52.1. Implementasi JSON di Python

# %% ◉ Membaca JSON file

import json

data = []
with open('data.json', 'r') as f:
    data = json.loads(f.read())

for key in data:
    print(f"{key}: {data[key]}")
