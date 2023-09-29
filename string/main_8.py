# %% A.17.9. Operasi string lainnya

# %% ◉ Replace substring

str_old = "hello world"
str_new = str_old.replace("world", "python")
print(str_new)

# %% ◉ Trim / strip

str = """
hello python
"""

print(f"--{str}--")
print(f"--{str.lstrip()}--")
print(f"--{str.rstrip()}--")
print(f"--{str.strip()}--")

# %% ◉ Join string

data = ["hello", "world", "abcdef"]
res = "-".join(data)
print(res)
