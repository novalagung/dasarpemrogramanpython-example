# %% A.17.4. String formatting

str = f"this is also a string in python"
print(str)

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
