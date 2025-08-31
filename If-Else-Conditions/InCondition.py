#This is a very common and readable way to see if something exists within a collection of items.

allowed_fruits = ["banana", "apple", "jackfruit"]
my_fruit = "orange"

if my_fruit in allowed_fruits:
    print(f"{my_fruit} is not allowed.")
else:
    print(f"Voila!! {my_fruit} is allowed now!")

print(type(allowed_fruits))