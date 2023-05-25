# %% A.8.2. Keyword elif

str_input = input('Enter your grade: ')
grade = int(str_input)

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("awesome")
elif grade >= 65:
    print("passed the exam")

# %% ◉ Fungsi input()

str_input = input('Enter your grade: ')
print("inputan user:", str_input, type(str_input))

# %% ◉ Type conversion / konversi tipe data

str_input = input('Enter your grade: ')
grade = int(str_input)
print("inputan user:", grade, type(grade))