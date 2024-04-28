# A.51.1. Implementasi JSON di Python

# %% ◉ Menulis data JSON ke file

jstr = """
[{
    "name": "Maiev Shadowsong",
    "affliations": ["Warden", "Alliance"],
    "age": 10000
}, {
    "name": "Illidan Stormrage",
    "affliations": ["Illidari", "Armies of Legionfall"],
    "age": 15000
}]
"""

with open('data.json', 'w') as f:
    f.write(jstr)

# %%

import json

data = {
    'name': 'Maiev Shadowsong',
    'affliations': ['Warden', 'Alliance']
}
jstr = json.dumps(data)

with open('data.json', 'w') as f:
    f.write(jstr)
