# %% A.47.7. Mengosongkan isi file

with open("file.txt", "w", encoding="utf-8") as f:
    pass

with open("file.txt", "w", encoding="utf-8"):
    pass

open("file.txt", "w", encoding="utf-8").close()

# %%

with open("file.txt", "w", encoding="utf-8") as f:
    f.truncate()
