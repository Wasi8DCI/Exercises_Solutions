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

def is_student(user):
    return user['type'] == 'student'

def show_offers(username, password):
    user = get_user(username, password)
    if not user or is_student(user):
        print("We have great courses to offer you!")
    else:
        print("You are a teacher, no offers for you!")


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
show_offers(username, password)

