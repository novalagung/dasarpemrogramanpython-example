# %% A.38.2. Custom decorator

def inspeksi(func):
    def inner_func():
        return func()
    return inner_func

@inspeksi
def say_hello():
    print("hello world")

say_hello()

inspeksi(say_hello)()

# %%

def inspeksi(func):
    def inner_func():
        print("fungsi ini akan dipanggil", func)
        res = func()
        print("fungsi telah selesai dieksekusi, nilai baliknya:", res)
        return res

    return inner_func

@inspeksi
def say_hello():
    print("hello world")

say_hello()
