# ### The while Loop
# Think of a while loop as saying, "Keep doing this action as long as this condition remains true."

# A very important warning: You must have a way for the condition to eventually become False. O
# therwise, you'll create an infinite loop, and your program will never end!

# Here are 3 examples:
# Example 1: A simple countdown
# We'll start a counter at 5 and loop as long as it's greater than 0. The line count = count - 1 is crucial to prevent an infinite loop.

counter = 5
while counter > 0:
    print(counter)
    counter = counter * 3