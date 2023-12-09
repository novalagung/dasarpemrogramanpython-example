# %% A.39.4. Chaining decorator ➜ ◉ Tahap 2: Decorator unique & reverse | Tahap 3: Decorator dipergunakan

import random

def generate_random_list(length):
    r = []

    for _ in range(0, length):
        n = random.randint(0, 10)
        r.append(n)
    
    return r

def decorator_unique_list(func):

    def execute(length):
        data = func(length)
        s = set(data)
        r = list(s)
        return r

    return execute

def decorator_reverse_list(func):

    def execute(length):
        data = func(length)
        data.sort(reverse=True)
        return data

    return execute

@decorator_unique_list
def generate_random_unique_list(length):
    return generate_random_list(length)

print("data from generate_random_unique_list():", generate_random_unique_list(15))

@decorator_reverse_list
def generate_random_reverse_sorted_list(length):
    return generate_random_list(length)

print("data from generate_random_reverse_sorted_list():", generate_random_reverse_sorted_list(15))
