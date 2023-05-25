# %% A.8.4. Seleksi kondisi bercabang / nested

str_input = input('Enter your grade: ')
grade = int(str_input)

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("awesome")
elif grade >= 65:
    print("passed the exam")
    if grade <= 70:
        print("but you need to improve it!")
    else:
        print("with ok grade")
else:
    print("below the passing grade")
