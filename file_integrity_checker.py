import hashlib

filename = input("Enter file path: ")

with open(filename, "rb") as file:
    data = file.read()

hash_value = hashlib.sha256(data).hexdigest()

print("SHA-256:")
print(hash_value)