import hashlib

filename = input("File path: ")

with open(filename, "rb") as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()

print("SHA-256:", file_hash)