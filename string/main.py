# %% basic string
str = "hello python"
print(str)

str = 'hello python'
print(str)

str = 'this is a "string" in python'
print(str)

str = "this is a \"string\" in python"
print(str)

str = """
a multiline string
in python
"""
print(str)

str = f"this is also a string in python"
print(str)

# %% string len()

str = "hello python"
print(len(str))

# %% string concatenation

str = "hello " "python"
print(str)

str_one = "hello"
str_two = "python"
str = str_one + " " + str_two
print(str)

str = " ".join(["hello", "python"])
print(str)

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

# %% if - in

str = "hello python"
if "py" in str:
    print(f"py is in {str}")

# %%

print(chr(4))

# chr()	Converts an integer to a character
# ord()	Converts a character to an integer

# %%

str = "hello python"
print(str.capitalize())
print(str.title())
print(str.upper())

str = "Hello Python"
print(str.lower())
print(str.swapcase())

# s.isalnum()

# s.isalpha()

# s.isdigit()

# s.isidentifier()

# s.islower()

# s.isprintable()

# s.isspace()

# s.istitle()

# s.isupper()

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





# %%
