# %%
n = int(input("enter max data: "))
i = 0

while i < n:
    print("number", i)
    i += 1

# %%
n = int(input("enter max data: "))

for i in range(n):
    print("number", i)

# %%
n = int(input("enter max data: "))
i = 0

while i < n:
    j = 0

    while j < n - i:
        print("*", end=" ")
        j += 1
    
    print()
    i += 1

# %%
n = int(input("enter max data: "))
i = 0

for i in range(n):
    j = 0

    while j < n - i:
        print("*", end=" ")
        j += 1
    
    print()
