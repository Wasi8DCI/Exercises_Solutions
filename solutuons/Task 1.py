username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}

while password == valid["password"] and username == valid["username"]:
    print("Welcome, admin!")
    break
else:
    print("Credentials are invalid")