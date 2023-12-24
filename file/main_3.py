# %% A.48.3. Menulis file

with open("file.txt", "w", encoding="utf-8") as f:
    f.write("hello")
    f.write("python\n")
    f.write("how are you?\n")
