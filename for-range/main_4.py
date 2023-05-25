# %% A.9.4. Perulangan bercabang / nested for

max = int(input("jumlah bintang: "))

for i in range(max):
    for j in range(0, max - i):
        print("*", end=" ")
    print()
