#Let's check a user's role and print a different welcome message.

#user_role = "editsdfgor"
user_role = str(input("Please enter your designation: "))


if user_role == "editor":
    print(f"Hello editor sir")
elif user_role == "admin":
    print(f"Yo!! Admin, how are you?")
else:
    print("The user role doesn't exists")
