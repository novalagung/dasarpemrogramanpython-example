# %% A.26.2. lambda return value

def get_hello_message1():
    return "hello python"

print(get_hello_message1())

get_hello_message2 = lambda : "hello python"

print(get_hello_message2())
