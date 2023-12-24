# %% A.43.2. Pencocokan pola data sequence

command = input("Enter command: ")
inputs = command.split(' ')

match inputs:

    case ["greet"]:
        name = input("Your name: ")
        print("hello", name)

    case ["greet", "thrall"]:
        print("hello Thrall, how is the horde?")

    case ["sum_numbers"]:
        numbers = input("The numbers separated by space: ")
        total = 0
        for str in numbers.split(' '):
            total = total + int(str)
        print("total:", total)

    case _:
        print("unrecognized command")

# %% ◉ Pencocokan sebagian pola

command = input("Enter command: ")

match command.split(' '):

    case ["greet"]:
        name = input("Your name: ")
        print("hello", name)

    case ["greet", "thrall"]:
        print("hello noval, how is the horde?")

    case ["greet", name]:
        print("hello", name)

    case _:
        print("unrecognized command")

# %% ◉ Pencocokan pola `*args`

command = input("Enter command: ")

match command.split(' '):

    case ["greet"]:
        name = input("Your name: ")
        print("hello", name)

    case ["greet", "thrall"]:
        print("hello noval, how is the horde?")

    case ["greet", name]:
        print("hello", name)

    case ["sum_numbers"]:
        numbers = input("The numbers separated by space: ")
        total = 0
        for str in numbers.split(' '):
            total = total + int(str)
        print("total:", total)

    case ["sum_numbers", *args]:
        total = 0
        for str in args:
            total = total + int(str)
        print("total:", total)
    
    case _:
        print("unrecognized command")

# %% Pencocokan pola wildcard

command = input("Enter command: ")

match command.split(' '):

    case ["greet"]:
        name = input("Your name: ")
        print("hello", name)

    case ["greet", "thrall"]:
        print("hello noval, how is the horde?")

    case ["greet", name]:
        print("hello", name)

    case ["sum_numbers"]:
        numbers = input("The numbers separated by space: ")
        total = 0
        for str in numbers.split(' '):
            total = total + int(str)
        print("total:", total)

    case ["sum_numbers", *args]:
        total = 0
        for str in args:
            total = total + int(str)
        print("total:", total)

    case [other]:
        print(f"unrecognized command {other}")

    case other:
        print(f"command {other} is not recognized")
