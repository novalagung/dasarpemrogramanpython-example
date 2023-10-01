# %% ◉ Konversi data ke string

number = 24
string1 = str(number)
print(string1)

items = [1, 2, 3, 4]
string2 = str(items)
print(string2)

obj = {
    "name": "AMD Ryzen 5600g",
    "type": "processor",
    "igpu": True,
}
string3 = str(obj)
print(string3)

# %%

number = 24
string1 = f"{number}"
print(string1)

items = [1, 2, 3, 4]
string2 = f"{items}"
print(string2)

obj = {
    "name": "AMD Ryzen 5600g",
    "type": "processor",
    "igpu": True,
}
string3 = f"{obj}"
print(string3)
