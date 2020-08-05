""" Description :   You will write a program that ask to enter a number (N) and display N times a random number between 1 and 100 
    Requirements :  ● Program must be named : ​09_random_loop.py and saved into week01/ex folder 
    Hint :  ❖ print function 
            ❖ random 
            ❖ loop
"""

# import random library
import random

# declaration boolean variable
program_is_running = True
# check loop condition
while program_is_running == True:
    # user input
    numInput = input("Enter a number: ")
    # check condition is digit or not
    if numInput.isdigit() == True:
        # convert string to number or integer
        x = int(numInput)
        # check the loop condition
        for i in range(x):
            # print output randomly between 1 and 100
            print(random.randint(1,100))
        exit()
    # check other conditions
    else:
        print("Wrong input!")
