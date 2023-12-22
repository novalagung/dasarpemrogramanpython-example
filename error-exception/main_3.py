# %% A.44.3. Throw exception

print("this program prints number from 0 to N")
n = int(input("enter the value of N: "))

if n <= 0:
    raise Exception("we do not allow 0 or negative number")

for d in range(0, n):
    print(d + 1)
