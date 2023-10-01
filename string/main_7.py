# %% A.17.8. Operasi pencarian string & substring

# %% ◉ Pengecekan string menggunakan keyword in

text = "hello world"
print("ello" in text)

if "ello" in text:
    print(f"py is in {text}")

# %% ◉ Pengecekan awalan dan akhiran string

print("hello world".startswith("hell"))
print("hello world".startswith("ello"))

print("hello world".endswith("orld"))
print("hello world".endswith("worl"))

print("hello world".count("ello"))

# %% ◉ Pencarian index substring

text = "hello world hello world"

print(text.count("ello"))

substring = "worl"
print(text.index(substring))
print(text.rindex(substring), text[18:])

print(text.find("worl"))
print(text.rfind("worl"))

# %%
