# %% A.17.8. Operasi pencarian string & substring

# %% ◉ Pengecekan string menggunakan keyword in

str = "hello world"
print("ello" in str)

if "ello" in str:
    print(f"py is in {str}")

# %% ◉ Pengecekan awalan dan akhiran string

str = "hello world"
print(str.startswith("hell"))
print(str.startswith("ello"))

str = "hello world"
print(str.endswith("orld"))
print(str.endswith("worl"))

str = "hello world"
print(str.count("ello"))

str = "hello world"
print(str.index("worl"))
# // error on failure

str = "hello world"
print(str.rindex("worl"))

str = "hello world"
print(str.find("worl"))

str = "hello world"
print(str.rfind("worl"))
