# %% A.7.7. Operator membership (in)

sample_list = [2, 3, 4]
is_3_exists = 3 in sample_list
print(is_3_exists)
# False

sample_tuple = ("hello", "python")
is_hello_exists = "hello" in sample_tuple
print(is_hello_exists)
# True

sample_dict = { "nama": "noval", "age": 12 }
is_key_nama_exists = "nama" in sample_dict
print(is_key_nama_exists)
# True

sample_set = { "sesuk", "preiiii" }
is_prei = "preiiii" in sample_set
print(is_prei)
# True

text = 'Hello world'
is_substring_exists = 'orl' in text
print(is_substring_exists)
# True
