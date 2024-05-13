# %% A.59.2. Generator function

def random_messages():
    yield "hello python"
    yield "how are you"
    yield "nice to meet you"

messages = random_messages()
print(messages)

for message in random_messages():
    print(message)

# %%

gen = random_messages()

message = next(gen)
print(f"message 1: {message}")

message = next(gen)
print(f"message 2: {message}")

message = next(gen)
print(f"message 3: {message}")

# %% ◉ Infinite counter

def infinite_counter():
    i = 0
    while True:
        yield i
        i = i + 1

c = infinite_counter()
print(next(c))
print(next(c))
print(next(c))

# %% ◉ Operasi baca file

def file_reader(file_name):
    for row in open(file_name, "r"):
        yield row

for row in open('content.txt'):
    print(row.strip())
