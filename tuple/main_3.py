# %% A.14.4. Perulangan data tuple

tuple_2 = ('ultra instinc shaggy', 'nightwing', 'noob saibot')

for t in tuple_2:
    print(t)

for i in range(0, len(tuple_2)):
    print("index:", i, "elem:", tuple_2[i])

for i, v in enumerate(tuple_2):
    print("index:", i, "elem:", v)
