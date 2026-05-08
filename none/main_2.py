# %% A.32.2. Penggunaan operator `is` terhadap `None`

def format_data(data):
    if data is not None:
        print(f"data: {data}")
    else:
        print("no data")

format_data("hello")
# output ➜ data: hello

format_data(None)
# output ➜ no data
