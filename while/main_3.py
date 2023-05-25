# %% A.10.3. Perulangan bercabang / nested while

n = int(input("enter max data: "))
i = 0

while i < n:
    j = 0

    while j < n - i:
        print("*", end=" ")
        j += 1
    
    print()
    i += 1
