# %% A.46.3. Keyword `try` + `except` + `else`

try:
    total_banana = int(input("total banana: "))
    total_people = int(input("number of person: "))
    res = total_banana / total_people
except ValueError as err:
    print(f"oops! not valid number detected. {err}")
except ZeroDivisionError as err:
    print(f"oops! unable to distribute banana because there is no person available. {err}")
except Exception as err:
    print(f"oops! something wrong. {err}")
else:
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
