# %% A.24.2. Kwargs

def print_data(**data):
    print(f"type: {type(data)}")
    print(f"data: {data}")
    print()
    for key in data:
        print(f"param: {key}, value: {data[key]}")

print_data(phone="nokia 3310", discontinue=False, year=2000, networks=["GSM", "TDMA"])

# %% ◉ Kombinasi positional argument dan kwargs

def print_data(message, number, **data):
    print(f"message: {message}")
    print(f"number: {number}")
    print()
    for key in data:
        print(f"param: {key}, value: {data[key]}")

print_data("sesuk prei", 2023, phone="nokia 3315", networks=["GSM", "TDMA"])

# %% ◉ Kombinasi positional argument, args dan kwargs

def print_all(message, *params, **others):
    print(f"message: {message}")
    print(f"params: {params}")
    print(f"others: {others}")

print_all("hello world", 1, True, ("yesn't", "nope"), name="nokia 3310", discontinued=True, year_released=2000)

# %% ◉ Kombinasi positional argument, args, keyword argument, dan kwargs

def print_all(message, *params, say_something, **others):
    print(f"message: {message}")
    print(f"params: {params}")
    print(f"say_something: {say_something}")
    print(f"others: {others}")

print_all("hello world", 1, True, ("yesn't", "nope"), say_something="how are you", name="nokia 3310", discontinued=True, year_released=2000)
