#Check if given number is positive, negetive or zero
number = int(input("Please enter a number: "))
print(f"Entered number is : {number}")

if number.is_integer:
    print("Given input is valid integer number. Now checking further...")
    if number == 0 or number > 0:
        print("Positive number")
    else:
        print("Negative number!")
else:
    print("The given number is not valid integer.")