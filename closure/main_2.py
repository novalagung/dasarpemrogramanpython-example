# %% A.25.2. Menampung fungsi/closure ke variabel

def print_all(message, *numbers, **others):
    print(f"message: {message}")
    print(f"numbers: {numbers}")
    print(f"others: {others}")

display = print_all
display("hello world", 1, 2, 3, 4, name="nokia 3310", discontinued=True, year_released=2000)
