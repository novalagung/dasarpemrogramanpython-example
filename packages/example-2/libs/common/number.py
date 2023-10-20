note = "module libs.common.number contains numerical functions"

def pow(n, p = 2):
    return n ** p

def sqrt(x):
    n = 1
    for _ in range(10):
        n = (n + x/n) * 0.5
    return n
