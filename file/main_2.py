# %% A.48.2. Keyword `with`

with open("file.txt", "w", encoding="utf-8") as f:
    print("file is closed:", f.closed)
    # ...

print("file is closed:", f.closed)
