# %% A.47.9. Mengecek apakah file ada

import os.path

if os.path.isfile("file.txt"):
    print("file.txt is exists")
else:
    print("file.txt is not exists")

# %%

if os.path.exists("/path/to/something"):
    print("something is exists")
else:
    print("something is not exists")

# %%

if os.path.exists("C:\\LibsSoftLink\\dasarpemrogramanpython\\examples\\file.txt"):
    print("file.txt is exists")
else:
    print("file.txt is not exists")
