failed_attempts = 0

while True:
    password = input("Enter password: ")

    if password == "MyPassword123":
        print("Login successful")
        break

    failed_attempts += 1
    print("Incorrect password")

    if failed_attempts >= 3:
        print("Account temporarily locked")
        break