users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

#You are registered to the module {modulename}.
# It will print this message if the user is a student and in his modules key has a module with a title equal to the argument modulename
#You did not register to the module {modulename}
# It will print this message if the user is anonymous or is a student and in his modules key DOES NOT have a module with the given title.
#You are a teacher It will print this message if the username is a teacher.


def show_registration(username, password, modulename):
    for user in users:
        if user["name"] == username and user["password"] == password and user["type"] == "Teacher":
            print("You are a teacher.")
            break
        if user["name"] == username and user["password"] == password and user["type"] == "student":
            for mod in user["modules"]:
                if modulename ==mod["title"]:
                    print(f"You are registered to the module {mod['title']}")
        if user["name"] == username and user["password"] == password and user["type"] == "student":
            for mod in user["modules"]:
                if modulename != mod["title"]:
                    print(f"You did not registered to the module {modulename}")
                    break
                break
    if user["name"] != username or user["password"] != password:
            print(f"You did not registered to the module {modulename}")

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)