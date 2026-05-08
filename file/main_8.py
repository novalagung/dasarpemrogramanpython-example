# %% A.50.8. Menghapus file

import os
from pathlib import Path

file_path = Path(__file__).resolve().parent / "file.txt"
file_path.write_text("temporary file", encoding="utf-8")
os.remove(file_path)

# target folder contoh yang portable lintas OS
target_dir = Path(__file__).resolve().parent / "tmp-example-dir"
target_dir.mkdir(exist_ok=True)
os.rmdir(target_dir)

# contoh lain penghapusan folder menggunakan path absolut
# (gunakan folder yang memang ada dan kosong)
another_dir = Path(__file__).resolve().parent / "tmp-example-dir-2"
another_dir.mkdir(exist_ok=True)
os.rmdir(another_dir)
