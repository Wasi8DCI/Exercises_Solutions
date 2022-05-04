users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]

def get_user(username, password):
    user_found = None
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return None

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
user = get_user(username, password)
# Rest of your code here

if not user:
    print("An error occurred. You are not authorized")