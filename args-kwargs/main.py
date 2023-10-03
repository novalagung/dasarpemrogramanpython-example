def sum_then_print(n1, n2, n3, n4, n5):
    total = n1 + n2 + n3 + n4 + n5
    print(total)

sum_then_print(2, 3, 4, 5, 4)

def sum_then_print(message, *numbers):
    total = 0
    for n in numbers:
        total = total + n
    print(f"{message} {total}")

sum_then_print("total nilai:", 2, 3, 4, 5, 4)

def concat_data_then_print(*data):
    text = ""
    for d in data:
        text = f"{text} {d}"
    print(text.strip())

concat_data_then_print("nokia 3310", True, 23.22, ("one", "two"), {"yesn't"})

# %%

def print_all(message, *numbers, **others):
    print(f"message: {message}")
    print(f"numbers: {numbers}")
    print(f"others: {others}")

print_all("hello world", 1, 2, 3, 4, name="nokia 3310", discontinued=True, year_released=2000)
