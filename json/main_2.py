# A.51.1. Implementasi JSON di Python

# %% ◉ Decode JSON string ke data Python

import json

jstr1 = '{ "name": "Maiev Shadowsong", "affliations": ["Warden", "Alliance"], "age": 10000, "active": true }'
data1 = json.loads(jstr1)

print(f"type: {type(data1).__name__}")

for key in data1:
    print(f"{key}: {data1[key]}")

# %%

jstr2 = """
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
data2 = json.loads(jstr2)

print(f"type: {type(data2).__name__}")

for row in data2:
    print(f"-> name: {row["name"]}, afflications: {row["affliations"]}, age: {row["age"]}")
