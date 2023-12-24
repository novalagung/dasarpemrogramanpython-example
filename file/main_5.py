# %% A.48.5. Membaca file

with open("file.txt", "r", encoding="utf-8") as f:
    print(f"line 1: {f.readline()}")
    print(f"line 2: {f.readline()}")
    print(f"line 3: {f.readline()}")
    print(f"line 4: {f.readline()}")
    print(f"line 5: {f.readline()}")

# %%

with open("file.txt", "r", encoding="utf-8") as f:
    i = 1
    while True:
        line = f.readline()
        if not line:
            break
        print(f"line {i}: {line}")
        i += 1

# %%

with open("file.txt", "r", encoding="utf-8") as f:
    i = 1
    for line in f:
        print(f"line {i}: {line}")
        i += 1

# %%

with open("file.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        print(f"line {i+1}: {line}")

# %%

with open("file.txt", "r", encoding="utf-8") as f:
    print(f.read())
