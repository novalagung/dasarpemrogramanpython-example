# %% A.50.9. Mengecek apakah file ada

import os.path
from pathlib import Path

if os.path.isfile("file.txt"):
    print("file.txt is exists")
else:
    print("file.txt is not exists")

# %%

# path contoh yang portable
path_location = Path(__file__).resolve().parent / "something"
if os.path.exists(path_location):
    print("something is exists")
else:
    print("something is not exists")

# %%

file_path = Path(__file__).resolve().parent / "file.txt"
if os.path.exists(file_path):
    print("file.txt is exists")
else:
    print("file.txt is not exists")
