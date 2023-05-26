# %% A.14.5. List dan tuple

data = [
    ("ultra instinc shaggy", 1, True, ['detective', 'saiyan']),
    ("nightwing", 3, True, ['teen titans', 'bat family']),
]

data.append(("noob saibot", 6, False, ['brotherhood of shadow']))
data.append(("tifa lockhart", 2, True, ['avalanche']))

print("name | rank | win | affliation")
print("------------------------------")

for row in data:
    for cell in row:
        print(cell, end=" | ")
    print()
