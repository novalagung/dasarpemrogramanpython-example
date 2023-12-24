# %% A.48.6. Membaca dan menulis dalam 1 sesi

with open("file.txt", "r+", encoding="utf-8") as f:
    print(f"read 1:\n{f.read()}")
    f.write("lorem ipsum dolor\n")
    print(f"read 2:\n{f.read()}")

with open("file.txt", "r+", encoding="utf-8") as f:
    print(f"read 3:\n{f.read()}")
