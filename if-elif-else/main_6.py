# %% A.8.6. Seleksi kondisi sebaris & ternary

# %% example 1

grade = int(input('Enter your grade: '))
if grade >= 65:
    print("passed the exam")
else:
    print("below the passing grade")

# %% example 2

grade = int(input('Enter your grade: '))
if grade >= 65: print("passed the exam")
if grade < 65: print("below the passing grade")

# %% example 3

grade = int(input('Enter your grade: '))
print("passed the exam") if grade >= 65 else print("below the passing grade")

# %% example 4

grade = int(input('Enter your grade: '))
message = "passed the exam" if grade >= 65 else "below the passing grade"
print(message)
