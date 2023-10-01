# %% A.17.5. Penggabungan string (concatenation)

text = "hello " "python"
print(text)

text_one = "hello"
text_two = "python"
text = text_one + " " + text_two
print(text)

text = "hello"
number = 123
yes = True
message = text + " " + str(number) + " " + str(yes)
print(message)

text = " ".join(["hello", "python"])
print(text)
