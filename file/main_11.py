# %% A.46.11. Menampilkan isi folder

import os

path_location = "C:\\LibsSoftLink\\dasarpemrogramanpython\\examples\\file"
for f in os.listdir(path_location):
    print(f)

# %%

import os

path_location = "C:\\LibsSoftLink\\dasarpemrogramanpython\\examples\\file"
for (dirpath, dirnames, filenames) in os.walk(path_location):
    print(dirpath, dirnames, filenames)

# %%

import glob

path_location = "C:\\LibsSoftLink\\dasarpemrogramanpython\\examples\\file"
for f in glob.glob(f"{path_location}\\**", recursive=True):
    print(f)
