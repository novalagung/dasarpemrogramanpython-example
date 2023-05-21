# %% numeric types

# int
number_1 = 10000024
print(number_1)

# float
number_2 = 3.14
print(number_2)

# complex
number_3 = 120+3j
print(number_3)

# %% string types

string_1 = "hello python"
print(string_1)

string_2 = """Selamat
Belajar
Python"""
print(string_2)

string_3 = 'for the horde!'
print(string_3)

string_4 = '''
Sesuk
Preiiii
'''
print(string_4)

string_5 = '''\
Sesuk
Preiiii
'''
print(string_5)

# %% bool

bool_1 = True
print(bool_1)

bool_2 = False
print(bool_2)

# %% list

# list with int as element's data type
list_1 = [2, 4, 8, 16]
print(list_1)

# list with str as element's data type
list_2 = ["grayson", "jason", "tim", "damian"]
print(list_2)

# list with various data type in the element
list_3 = [24, False, "Hello Python"]
print(list_3)

# acces item by index
print(list_1[2])

# %% tuple

# tuple with int as element's data type
tuple_1 = (2, 3, 4)
print(tuple_1)

# tuple with str as element's data type
tuple_2 = ("numenor", "valinor")
print(tuple_2)

# tuple with various data type in the element
tuple_3 = (24, False, "Hello Python")
print(tuple_3)

# acces item by index
print(tuple_1[2])

# %% dictionary

profile_1 = {
  "name": "Noval",
  "is_male": False,
  "age": 16,
  "hobbies": ["gaming", "learning"]
}

print("name: %s" % (profile_1["name"]))
print("hobbies: %s" % (profile_1["hobbies"]))

# %% sets

set_1 = {"pineapple", "spaghetti"}
print(set_1)
