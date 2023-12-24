# %% A.46.2. Explicit exception handler

try:
    total_banana = int(input("total banana: "))
    total_people = int(input("number of person: "))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except ValueError:
    print("oops! not valid number detected")
except ZeroDivisionError:
    print("oops! unable to distribute banana because there is no person available")

# %% ◉ Menangkap banyak exception sekaligus

try:
    total_banana = int(input("total banana: "))
    total_people = int(input("number of person: "))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except (ValueError, ZeroDivisionError):
    print("oops! something wrong")

# %% ◉ Menangkap semua exception

try:
    total_banana = int(input("total banana: "))
    total_people = int(input("number of person: "))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except:
    print("oops! something wrong")

try:
    total_banana = int(input("total banana: "))
    total_people = int(input("number of person: "))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except Exception:
    print("oops! something wrong")

# %% ◉ Memunculkan pesan exception

try:
    total_banana = int(input("total banana: "))
    total_people = int(input("number of person: "))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except ValueError as err:
    print(f"oops! not valid number detected. {err}")
except ZeroDivisionError as err:
    print(f"oops! unable to distribute banana because there is no person available. {err}")
except Exception as err:
    print(f"oops! something wrong. {err}")

# %% ◉ Alternatif penulisan exception

try:
    total_banana = int(input("total banana: "))
    total_people = int(input("number of person: "))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except Exception as err:
    if err == ValueError:
        print(f"oops! not valid number detected. {err}")
    elif err == ZeroDivisionError:
        print(f"oops! unable to distribute banana because there is no person available. {err}")
    else:
        print(f"oops! something wrong. {err}")
