# %% Lambda parameter fungsi/closure/lambda

aggregate = lambda message, numbers, f: print(f"{message} is {f(numbers)}")

numbers = [24, 67, 22, 98, 3, 50]

def average1(numbers):
    return sum(numbers) / len(numbers)

aggregate("average", numbers, average1)

average2 = lambda numbers : sum(numbers) / len(numbers)
aggregate("average", numbers, average2)

aggregate("average", numbers, lambda numbers : sum(numbers) / len(numbers))
