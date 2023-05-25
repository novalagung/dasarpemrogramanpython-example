# %% A.9.3. Perulangan for tanpa range()

# %% ◉ Iterasi data list

messages = ["morning", "afternoon", "evening"]
for m in messages:
    print(m)

# %% ◉ Iterasi data tuple

numbers = ("twenty four", 24)
for n in numbers:
    print(n)

# %% ◉ Iterasi data string

for char in "hello python":
    print(char)

# %% ◉ Iterasi data dictionary

bio = {
    "name": "toyota camry",
    "year": 1993,
}

for key in bio:
    print("key:", key, "value:", bio[key])

# %% ◉ Iterasi data sets

numbers = {"twenty four", 24}
for n in numbers:
    print(n)
