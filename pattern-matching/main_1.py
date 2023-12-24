# A.43.1. Pengenalan pattern matching

command = input("Enter command: ")

if command == "greet":
    name = input("Your name: ")
    print("hello", name)

elif command == "find sum of numbers":
    numbers = input("The numbers separated by space: ")
    total = 0
    for str in numbers.split(' '):
        total = total + int(str)
    print("total:", total)

elif command == "lucky number":
    import random
    n = random.randint(0, 100)
    print("your lucky number:", n)

else:
    print("unrecognized command")

# %%

command = input("Enter command: ")

match command:

    case "greet":
        name = input("Your name: ")
        print("hello", name)

    case "sum_numbers":
        numbers = input("The numbers separated by space: ")
        total = 0
        for str in numbers.split(' '):
            total = total + int(str)
        print("total:", total)

    case "lucky_number":
        import random
        n = random.randint(0, 100)
        print("your lucky number:", n)
    
    case _:
        print("unrecognized command")
