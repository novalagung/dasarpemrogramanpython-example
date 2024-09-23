# %% A.11.3. Label perulangan

max = int(input("jumlah bintang: "))

outer_loop = True
for i in range(max):
    if not outer_loop: 
        break

    for j in range(i + 1):
        print("*", end=" ")
        if j >= 7:
            outer_loop = False
            break
    print()
