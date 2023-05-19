#%% if

grade = 100

if grade == 100:
    print("perfect")

if grade == 90:
    print("ok")
    print("keep working hard!")

#%% if elif

str_input = input('Enter your grade: ')
grade = int(str_input)

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("awesome")
elif grade >= 65:
    print("passed the exam")

#%% input

str_input = input('Enter your grade: ')
print("inputan user:", str_input, type(str_input))

#%% type conversion

str_input = input('Enter your grade: ')
grade = int(str_input)
print("inputan user:", grade, type(grade))

#%% if elif else

str_input = input('Enter your grade: ')
grade = int(str_input)

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("awesome")
elif grade >= 65:
    print("passed the exam")
else:
    print("below the passing grade")

#%% netsted if

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

#%% logical operator

grade = int(input('Enter your current grade: '))
prev_grade = int(input('Enter your previous grade: '))

if grade >= 90 and prev_grade >= 65:
    print("awesome")
if grade >= 90 and prev_grade < 65:
    print("awesome. you definitely working hard, right?")
elif grade >= 65:
    print("passed the exam")
else:
    print("below the passing grade")

if (grade >= 65 and not prev_grade >= 65) or (not grade >= 65 and prev_grade >= 65):
    print("at least you passed one exam. good job!")

#%% one line

grade = int(input('Enter your grade: '))

# example 1
if grade >= 65:
    print("passed the exam")
else:
    print("below the passing grade")

# example 2
if grade >= 65: print("passed the exam")
if grade < 65: print("below the passing grade")

# example 3
print("passed the exam") if grade >= 65 else print("below the passing grade")

# example 4
message = "passed the exam" if grade >= 65 else "below the passing grade"
print(message)
