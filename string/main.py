
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
