def outer_func(numbers = []):
    print("from outer_func")
    print(f"numbers: {numbers}")

    def inner_func():
        print("from inner_func")
        print(f"max: {max(numbers)}")
        print(f"min: {min(numbers)}")
    
    return inner_func

f = outer_func([1, 2, 3, 4])
print()
f()

# %%

def print_all(message, *numbers, **others):
    print(f"message: {message}")
    print(f"numbers: {numbers}")
    print(f"others: {others}")

display = print_all
display("hello world", 1, 2, 3, 4, name="nokia 3310", discontinued=True, year_released=2000)
