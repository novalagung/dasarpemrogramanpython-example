# %% A.10.4. Kombinasi while dan for

n = int(input("enter max data: "))
i = 0

for i in range(n):
    j = 0

    while j < n - i:
        print("*", end=" ")
        j += 1
    
    print()
