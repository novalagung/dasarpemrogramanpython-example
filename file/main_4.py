# %% A.49.4. Append konten ke file

with open("file.txt", "a", encoding="utf-8") as f:
    f.write("happy monday\n")
