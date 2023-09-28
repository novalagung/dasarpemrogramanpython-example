
# %%

str = "hello python"
print(str.capitalize())
print(str.title())
print(str.upper())

str = "Hello Python"
print(str.lower())
print(str.swapcase())

# %%

print("123abc".isalnum())
print("abcdef".isalpha())
print("123456".isdigit())

print(" ".isspace())

print("hello python".islower())
print("Hello Python".istitle())
print("HELLO PYTHON".isupper())

# %%



# s.isprintable()
# s.isidentifier()

# s.count(<sub>[, <start>[, <end>]])

# s.endswith(<suffix>[, <start>[, <end>]])

# s.find(<sub>[, <start>[, <end>]])

# s.index(<sub>[, <start>[, <end>]])

# s.rfind(<sub>[, <start>[, <end>]])

# s.rindex(<sub>[, <start>[, <end>]])

# s.startswith(<prefix>[, <start>[, <end>]])

# s.center(<width>[, <fill>])

# s.expandtabs(tabsize=8)

# s.ljust(<width>[, <fill>])

# s.lstrip([<chars>])

# s.replace(<old>, <new>[, <count>])

# s.rjust(<width>[, <fill>])

# s.rstrip([<chars>])

# s.strip([<chars>])

# s.zfill(<width>)

# s.join(<iterable>)

# s.partition(<sep>)

# s.rpartition(<sep>)

# s.rsplit(sep=None, maxsplit=-1)

# s.split(sep=None, maxsplit=-1)

# s.splitlines([<keepends>])

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
