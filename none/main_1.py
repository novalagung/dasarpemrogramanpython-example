# %% A.31.1. Pengenalan `None`

def inspect_data(data):
    if data is None:
        print("data is empty. like very empty")
    else:
        print(f"data: {data}, type: {type(data).__name__}")

data = 0
inspect_data(data)

data = ""
inspect_data(data)

data = None
inspect_data(data)

class Car:
    def __init__(self):
        self.name = ""

data = Car()
inspect_data(data)
