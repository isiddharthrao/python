# Example 2: Waiting for a user to say "quit"
# This is a classic use case for while. The loop continues until the user types the magic word.

command = ""
while command.lower != "quit":
    print(f"Type 'quit' to exit.")
    command = input("Enter a command to quit: ")
    print(f"You've typed : {command}")
