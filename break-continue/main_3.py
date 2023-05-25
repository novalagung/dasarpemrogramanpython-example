# %% A.11.3. Label perulangan

max = int(input("jumlah bintang: "))

outerLoop = True
for i in range(max):
    if not outerLoop: 
        break

    for j in range(i + 1):
        print("*", end=" ")
        if j >= 7:
            outerLoop = False
            break
    print()
