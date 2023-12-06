# %% handling exception

def calculate_banana_distribution(total_banana, total_people):
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")

try:
    calculate_banana_distribution(75, 5)
    calculate_banana_distribution(25, 0)
except:
    print("oops! unable to distribute banana because there is no person available")

try:
    calculate_banana_distribution(75, 5)
    calculate_banana_distribution(25, 0)
except Exception:
    print("oops! unable to distribute banana because there is no person available")

try:
    calculate_banana_distribution(75, 5)
    calculate_banana_distribution(25, 0)
except Exception as err:
    print("oops! unable to distribute banana because there is no person available")
    print(f"error: {err}")

# %%

def calculate_banana_distribution(total_banana, total_people):
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")

try:
    calculate_banana_distribution(75, 5)
    calculate_banana_distribution(25, 0)
except ZeroDivisionError:
    print("oops! unable to distribute banana because there is no person available")

try:
    calculate_banana_distribution(75, 5)
    calculate_banana_distribution(25, 0)
except ZeroDivisionError as err:
    print(f"oops! unable to distribute banana because there is no person available. error: {err}")

# %%

def combine_data(data1, data2):
    res = data1 + data2
    print(f"combined data: {res}")

try:
    combine_data(23, 55)
    combine_data("23", 55)
except ZeroDivisionError:
    print("oops! unable to distribute banana because there is no person available")

try:
    combine_data(23, 55)
    combine_data("23", 55)
except ZeroDivisionError:
    print("oops! unable to distribute banana because there is no person available")
except TypeError:
    print("oops! combining two different data types should not be allowed")

try:
    combine_data(23, 55)
    combine_data("23", 55)
except (ZeroDivisionError, TypeError) as err:
    if err == ZeroDivisionError:
        print("oops! unable to distribute banana because there is no person available")
    elif err == TypeError:
        print("oops! combining two different data types should not be allowed")

# %% first exception fail

def combine_data(data1, data2):
    res = data1 + data2
    print(f"combined data: {res}")

try:
    calculate_banana_distribution(75, 5)
    calculate_banana_distribution(25, 0)

    combine_data(23, 55)
    combine_data("23", 55)
except ZeroDivisionError:
    print("oops! unable to distribute banana because there is no person available")
except TypeError:
    print("oops! combining two different data types should not be allowed")

# %% else

try:
    print("program to perform division over two numbers")
    n1 = int(input("enter 1st number: "))
    n2 = int(input("enter 2nd number: "))
    res = n1 / n2
except ZeroDivisionError as err:
    print(f"oops! unable to divide number by 0. error: {err}")
else:
    print(f"{n1} / {n2}: {res}")

# %%

try:
    print("program to perform division over two numbers")
    n1 = int(input("enter 1st number: "))
    n2 = int(input("enter 2nd number: "))
    res = n1 / n2
except ZeroDivisionError as err:
    print(f"oops! unable to divide number by 0. error: {err}")
finally:
    print(f"program completed")

try:
    print("program to perform division over two numbers")
    n1 = int(input("enter 1st number: "))
    n2 = int(input("enter 2nd number: "))
    res = n1 / n2
except ZeroDivisionError as err:
    print(f"oops! unable to divide number by 0. error: {err}")
else:
    print(f"{n1} / {n2}: {res}")
finally:
    print(f"program completed")
