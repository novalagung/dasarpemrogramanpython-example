# %%
while True:
    n = int(input("enter a number divisible by 3: "))
    if n % 3 != 0:
        break

    print("%d is divisible by 3" % (n))

# %%
for i in range(5):
    if i < 3 or i > 7:
        continue
    print(i)
