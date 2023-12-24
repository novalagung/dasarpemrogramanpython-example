# A.52.3. Pencocokan pola + seleksi kondisi

# %% ◉ Pencocokan pola + logika OR

command = input("Enter command: ")

match command.split(' '):

    case ["greet"]:
        name = input("Your name: ")
        print("hello", name)

    case ["greet", "thrall"]:
        print("hello noval, how is the horde?")

    case ["greet", name, ("morning" | "afternoon" | "evening") as t]:
        print("hello", name, "good", t)

    case ["greet", name] | ["hello", name]:
        print("hello", name)

    case ([other] | other) as o:
        print(f"command {o} is not recognized")

# %% ◉ Pencocokan pola + keyword `if`

command = input("Enter command: ")

match command.split(' '):

    case ["greet"]:
        name = input("Your name: ")
        print("hello", name)

    case ["greet", name] if name == "thrall":
        print("hello noval, how is the horde?")

    case ["greet", name, ("morning" | "afternoon" | "evening") as t]:
        print("hello", name, "good", t)

    case other:
        print(f"command {other} is not recognized")
