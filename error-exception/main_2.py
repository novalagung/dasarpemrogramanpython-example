# # %% A.43.2. Exception

n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))

res = n1 / n2
print(f"{n1} / {n2} = {res}")

# %%

n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))

if n2 == 0:
    print("we do not allow the value of 0 on the 2nd number")
else:
    res = n1 / n2
    print(f"{n1} / {n2} = {res}")
