# %% A.17.8. Operasi pencarian string & substring

# %% ◉ Pengecekan string menggunakan keyword in

str = "hello world"
print("ello" in str)

if "ello" in str:
    print(f"py is in {str}")

# %% ◉ Pengecekan awalan dan akhiran string

print("hello world".startswith("hell"))
print("hello world".startswith("ello"))

print("hello world".endswith("orld"))
print("hello world".endswith("worl"))

print("hello world".count("ello"))

# %% ◉ Pencarian index substring

str = "hello world hello world"

print(str.count("ello"))

substring = "worl"
print(str.index(substring))
print(str.rindex(substring), str[18:])

print(str.find("worl"))
print(str.rfind("worl"))

# %%
