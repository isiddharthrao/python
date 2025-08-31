# Example 4: Combining a for loop with an if statement
# Now we're getting powerful. Let's loop through a list of numbers and only print the ones that are even.

list_of_numbers = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 12, 14, 13, 17, 18, 21]

for number in list_of_numbers:
    if number % 2 == 0:
        print(f"{number} is even number")
        
