# %% A.17.8. Operasi string lainnya

# %% ◉ Replace substring

text_old = "hello world"
text_new = text_old.replace("world", "python")
print(text_new)

# %% ◉ Trim / strip

text = """
hello python
"""

print(f"--{text}--")
print(f"--{text.lstrip()}--")
print(f"--{text.rstrip()}--")
print(f"--{text.strip()}--")

# %% ◉ Join string

data = ["hello", "world", "abcdef"]
res = "-".join(data)
print(res)

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
