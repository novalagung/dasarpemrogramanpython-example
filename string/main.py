# %% string formatting

name = "Aiden Pearce"
occupation = "IT support"

str = f"hello, my name is {name}, I'm an {occupation}"
print(str)

str = "hello, my name is {name}, I'm an {occupation}".format(name = name, occupation = occupation)
print(str)

str = "hello, my name is {0}, I'm an {1}".format(name, occupation)
print(str)

str = "hello, my name is {}, I'm an {}".format(name, occupation)
print(str)

# %% String elements

str = "hello python"
print(str[0])
print(str[1])
print(str[2])

for c in str:
    print(c)

for i in range(0, len(str)):
    print(str[i])

# %% String slicing

str = "hello python"
print(str[1:5])
print(str[7:])
print(str[:4])

# %%

str = "hello python"
print(str.capitalize())
print(str.title())
print(str.upper())

str = "Hello Python"
print(str.lower())
print(str.swapcase())

# %%

str = "hello123"
print(str.isalnum())
str = "hello 123"
print(str.isalnum())

str = "hello"
print(str.isalpha())
str = "hello123"
print(str.isalpha())

str = "123"
print(str.isdigit())
str = "123four"
print(str.isdigit())

str = "hello world"
print(str.islower())
str = "Hello world"
print(str.islower())

str = "hello world"
print(str.istitle())
str = "Hello World"
print(str.istitle())
str = "Hello world"
print(str.istitle())

str = "HELLO WORLD"
print(str.isupper())
str = "Hello World"
print(str.isupper())

str = "\n"
print(str.isspace())
str = "\n\r"
print(str.isspace())
str = """
"""
print(str.isspace())
str = "hello world\n"
print(str.isspace())

# %%

str = "hello world"
print("ello" in str)

if "ello" in str:
    print(f"py is in {str}")

str = "hello world"
print(str.startswith("hell"))
print(str.startswith("ello"))

str = "hello world"
print(str.endswith("orld"))
print(str.endswith("worl"))

str = "hello world"
print(str.count("ello"))

str = "hello world"
print(str.index("worl"))
# // error on failure

str = "hello world"
print(str.rindex("worl"))

str = "hello world"
print(str.find("worl"))

str = "hello world"
print(str.rfind("worl"))

str_old = "hello world"
str_new = str_old.replace("world", "python")
print(str_new)

str = """
hello python
"""

print(str)
print(str.lstrip())
print(str.rstrip())
print(str.strip())

data = [1, 2, 3, 4]
res = "-".join(data)
print(res)

# s.partition(<sep>)
# s.rpartition(<sep>)

# s.split(sep=None, maxsplit=-1)
# s.rsplit(sep=None, maxsplit=-1)
# s.splitlines([<keepends>])

# s.center(<width>[, <fill>])
# s.ljust(<width>[, <fill>])
# s.rjust(<width>[, <fill>])

# str.zfill(<width>)
# s.expandtabs(tabsize=8)

# %%
