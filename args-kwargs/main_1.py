# %% A.24.1. args

def sum_then_print(n1, n2, n3, n4, n5):
    total = n1 + n2 + n3 + n4 + n5
    print(total)

sum_then_print(2, 3, 4, 5, 4)

# %%

def sum_then_print(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    print(total)

sum_then_print(2, 3, 4, 5, 4)

# %% ◉ Args untuk argument dengan tipe data bervariasi

def print_data(*params):
    print(f"type: {type(params)}, data: {params}")
    for i in range(len(params)):
        print(f"param {i}: {params[i]}")

print_data("hello python", 123, [5, True, ("yesn't")], {"iwak", "peyek"})

# %% ◉ Kombinasi positional argument dan args

def sum_then_print(message, *numbers):
    total = 0
    for n in numbers:
        total = total + n
    print(f"{message} {total}")

sum_then_print("total nilai:", 2, 3, 4, 5, 4)

# %% ◉ Kombinasi positional argument dan args

def sum_then_print(message, *numbers, suffix_message):
    total = 0
    for n in numbers:
        total = total + n
    print(f"{message} {total} {suffix_message}")

sum_then_print("total nilai:", 2, 3, 4, 5, 4, suffix_message="selesai!")
