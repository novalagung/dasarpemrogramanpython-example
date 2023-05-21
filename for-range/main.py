# %%
for i in range(5):
    print("index:", i)

# %%
r = range(5)
print("r:", list(r))

# %%
for i in range(3):
    print("index:", i)

for i in range(0, 3):
    print("index:", i)

for i in range(0, 3, 1):
    print("index:", i)

# %%
for i in range(2, 10, 2):
    print("index:", i)

for i in range(5, -5, -1):
    print("index:", i)

# %%
messages = ["morning", "afternoon", "evening"]
for m in messages:
    print(m)

# %%
numbers = ("twenty four", 24)
for n in numbers:
    print(n)

# %%
for char in "hello python":
    print(char)

# %%
bio = {
    "name": "toyota camry",
    "year": 1993,
}

for key in bio:
    print("key:", key, "value:", bio[key])

# %%
numbers = {"twenty four", 24}
for n in numbers:
    print(n)

# %%
max = int(input("jumlah bintang: "))

for i in range(max):
    for j in range(0, max - i):
        print("*", end=" ")
    print()
