# %% A.39.4. Chaining decorator

import random

def generate_random_list(length):
    r = []

    for _ in range(0, length):
        n = random.randint(0, 10)
        r.append(n)
    
    return r

def decorator_unique_list(func):

    def execute(length):
        print("decorator_unique_list | before", func)
        data = func(length)
        print("decorator_unique_list | after")
        s = set(data)
        r = list(s)
        return r

    return execute

def decorator_reverse_list(func):

    def execute(length):
        print("decorator_reverse_list | before", func)
        data = func(length)
        print("decorator_reverse_list | after")
        data.sort(reverse=True)
        return data

    return execute

@decorator_reverse_list
@decorator_unique_list
def generate_random_unique_reverse_sorted_list(length):
    return generate_random_list(length)

print("result:", generate_random_unique_reverse_sorted_list(15))

# %%
