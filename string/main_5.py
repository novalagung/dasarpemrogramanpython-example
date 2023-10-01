# %% A.17.6. Operasi sequence pada string

# %% ◉ Mengecek lebar karakter string

text = "hello python"
print("text:", text)
print("length:", len(text))

# %% String elements

text = "hello python"
print(text[0])
print(text[1])
print(text[2])

for c in text:
    print(c)

for i in range(0, len(text)):
    print(text[i])

# %% Slicing string

text = "hello python"
print(text[1:5])
print(text[7:])
print(text[:4])
