# %% A.50.12. pathlib.Path (modern file path handling)

from pathlib import Path

base_dir = Path(__file__).resolve().parent
sample_dir = base_dir / "pathlib-sample"
sample_file = sample_dir / "file.txt"

# membuat folder
sample_dir.mkdir(parents=True, exist_ok=True)

# menulis file
sample_file.write_text("hello python", encoding="utf-8")

# mengecek apakah file ada
if sample_file.is_file():
    print("file.txt is exists")

# membaca isi file
content = sample_file.read_text(encoding="utf-8")
print(content)

# menampilkan isi folder
for f in sample_dir.iterdir():
    print(f)

# menghapus file dan folder
sample_file.unlink(missing_ok=True)
sample_dir.rmdir()
