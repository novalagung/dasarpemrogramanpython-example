# %% A.49.2. Keyword `with`

with open("file.txt", "w", encoding="utf-8") as f:
    print("file is closed:", f.closed)
    # ...

print("file is closed:", f.closed)
