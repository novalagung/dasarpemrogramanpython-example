# %% A.50.10. Membuat folder baru

import os
from pathlib import Path

os.makedirs(Path(__file__).resolve().parent / "somefolder", exist_ok=True)

# %%

import os
from pathlib import Path

os.makedirs(Path(__file__).resolve().parent / "another-folder", exist_ok=True)
