
import os
import hashlib
from datetime import datetime

filename = input("Enter file path: ")

if os.path.isfile(filename):
    info = os.stat(filename)

    with open(filename, "rb") as file:
        sha256 = hashlib.sha256(file.read()).hexdigest()

    print("Filename:", os.path.basename(filename))
    print("File size:", info.st_size, "bytes")
    print("Last modified:",
          datetime.fromtimestamp(info.st_mtime))
    print("SHA-256:", sha256)
else:
    print("File not found")
