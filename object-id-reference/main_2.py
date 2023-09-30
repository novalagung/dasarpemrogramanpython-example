# %% A.21.2. Reference / alamat memori data

message1 = "hello world"
message2 = message1
message3 = "hello world"

print(f"var: message1, data: {message1}, id: {id(message1)}")
print(f"var: message2, data: {message2}, id: {id(message2)}")
print(f"var: message3, data: {message3}, id: {id(message3)}")

