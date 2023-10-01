# %% A.17.9. Operasi string lainnya

# %% ◉ Replace substring

text_old = "hello world"
text_new = text_old.replace("world", "python")
print(text_new)

# %% ◉ Trim / strip

text = """
hello python
"""

print(f"--{text}--")
print(f"--{text.lstrip()}--")
print(f"--{text.rstrip()}--")
print(f"--{text.strip()}--")

# %% ◉ Join string

data = ["hello", "world", "abcdef"]
res = "-".join(data)
print(res)
