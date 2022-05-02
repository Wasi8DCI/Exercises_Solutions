users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

def get_user(username, password):
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return None

def show_offers(username, password):
    user = get_user(username, password)
    if not user or user['type'] == 'student':
        print("We have great courses to offer you!")


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
show_offers(username, password)

