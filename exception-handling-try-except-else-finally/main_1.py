# %% A.44.1. Keyword `try` + `except`

def calculate_banana_distribution(total_banana, total_people):
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")

total_banana = 75
total_people = 3
calculate_banana_distribution(total_banana, total_people)

# %%

try:
    print("1st calculation")
    calculate_banana_distribution(75, 5)

    print("2nd calculation")
    calculate_banana_distribution(25, 0)

    print("3rd calculation")
    calculate_banana_distribution(15, 2)
except:
    print("oops! unable to distribute banana because there is no person available")

# %%

def calculate_banana_distribution(total_banana, total_people):
    try:
        res = total_banana / total_people
        print(f"in fair distribution, each person shall receive {res:.0f} banana")
    except:
        print("oops! unable to distribute banana because there is no person available")

print("1st calculation")
calculate_banana_distribution(75, 5)

print("2nd calculation")
calculate_banana_distribution(25, 0)

print("3rd calculation")
calculate_banana_distribution(15, 2)
