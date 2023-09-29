# %% A.17.6. Operasi sequence pada string

# %% ◉ Mengecek lebar karakter string

str = "hello python"
print("text:", str)
print("length:", len(str))

# %% String elements

str = "hello python"
print(str[0])
print(str[1])
print(str[2])

for c in str:
    print(c)

for i in range(0, len(str)):
    print(str[i])

# %% Slicing string

str = "hello python"
print(str[1:5])
print(str[7:])
print(str[:4])
