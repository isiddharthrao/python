#Let's determine if a number is even or odd. We use the modulo operator (%), which gives us the remainder of a division.

number = int(input("Please enter a number: "))

if number % 2==0:
    print(f"Given number is even.")
else:
    print(f"Odd number")