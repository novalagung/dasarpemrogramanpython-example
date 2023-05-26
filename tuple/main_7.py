# A.14.7. Tuple *packing* dan *unpacking*

# %% ◉ Tuple *packing*

first_name = "aerith gainsborough"
rank = 11
win = False

row_data = (first_name, rank, win)
# row_data = first_name, rank, win

print(row_data)

# %% ◉ Tuple *unpacking*

row_data = ('aerith gainsborough', 11, False)
first_name, rank, win = row_data

print(first_name, rank, win)
