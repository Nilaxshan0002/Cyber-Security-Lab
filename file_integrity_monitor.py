
import hashlib
import os

def get_hash(filename):
    with open(filename, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()

filename = input("Enter file path: ")

if not os.path.isfile(filename):
    print("File not found")
else:
    original_hash = get_hash(filename)

    print("Original SHA-256:", original_hash)
    input("Modify the file, then press Enter...")

    new_hash = get_hash(filename)

    if original_hash == new_hash:
        print("File unchanged")
    else:
        print("WARNING: File has changed!")
