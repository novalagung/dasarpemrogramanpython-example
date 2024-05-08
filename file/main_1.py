# %% A.49.1. Membuka stream file

f = open("file.txt", "w", encoding="utf-8")

# ...

f.close()

# %%

f = open("file.txt", "w", encoding="utf-8")
print("file is closed:", f.closed)

# ...

f.close()
print("file is closed:", f.closed)
