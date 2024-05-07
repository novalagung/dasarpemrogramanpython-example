# %%

my_var = 12

def task_one():
    all_global_vars = globals()
    print(all_global_vars['my_var'])

task_one()

# %%

my_var = 12

def task_two():
    another_var = "Hello Python"

    all_locals_vars = locals()
    print(all_locals_vars['another_var'])

    try:
        print(all_locals_vars['my_var'])
    except Exception as err:
        print(f'error {err}')

task_two()

# %%

def task_three():
    message = "Hola"
    print(len(locals()))
    print(len(globals()))

task_three()

# %%
