# %% A.50.11. Menampilkan isi folder

import os
from pathlib import Path

path_location = Path(__file__).resolve().parent
for f in os.listdir(path_location):
    print(f)

# %%

import os
from pathlib import Path

path_location = Path(__file__).resolve().parent
for (dirpath, dirnames, filenames) in os.walk(path_location):
    print(dirpath, dirnames, filenames)

# %%

import glob
from pathlib import Path

path_location = Path(__file__).resolve().parent
for f in glob.glob(f"{path_location}/**", recursive=True):
    print(f)
