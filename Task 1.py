username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}

while password == "admin" and username == "admin":
    print("Welcome, admin!")
    break
else:
    print("Credentials are invalid")