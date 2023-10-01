# %% A.17.4. String formatting

text = f"this is also a string in python"
print(text)

name = "Aiden Pearce"
occupation = "IT support"

text = f"hello, my name is {name}, I'm an {occupation}"
print(text)

text = "hello, my name is {name}, I'm an {occupation}".format(name = name, occupation = occupation)
print(text)

text = "hello, my name is {0}, I'm an {1}".format(name, occupation)
print(text)

text = "hello, my name is {}, I'm an {}".format(name, occupation)
print(text)
