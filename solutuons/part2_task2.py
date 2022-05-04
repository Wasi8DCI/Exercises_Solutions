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


#This time, the function will do nothing if the user is valid and a teacher.
#It will check if, besides having a particular module in the user's list,
# the module has the key completed set to True.

def has_completed_module(username, password, modulename):
    for user in users:
        if user["name"] == username and user["password"] == password and user["type"] == "Teacher":
            return user
        return None
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
has_completed_module(username, password, modulename)
