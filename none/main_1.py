# %% A.31.1. Pengenalan `None`

def inspec_data(data):
    if data == None:
        print("data is empty. like very empty")
    else:
        print(f"data: {data}, type: {type(data).__name__}")

data = 0
inspec_data(data)

data = ""
inspec_data(data)

data = None
inspec_data(data)

class Car:
    def __init__(self):
        self.name = ""

data = Car()
inspec_data(data)
