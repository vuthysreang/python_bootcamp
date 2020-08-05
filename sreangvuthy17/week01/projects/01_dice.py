"""
    PROJECT 01: Dice Roller
"""

import random
# declare the constant
INTRO_MESSAGE = 'Welcome to the dices game!'
# print output of constant
print(INTRO_MESSAGE)
# declare variable
i = 1
# declare variable
result = 0
# declare the boolean variable
running = True
# check loop condition
while running == True:
    # user input
    rollInput = input("Enter the number of dices you want to roll: ")
    # check the condition
    if rollInput == "" or rollInput.isdigit() == False:
        # print output if condition is True
        print("USAGE: The number must be between 1 and 8")
    # check the condition 
    elif int(rollInput) > 8 or int(rollInput) < 1:
        # print output if condition is True
        print("USAGE: The number must be between 1 and 8")
    # check other condition
    else:
        # we want to terminate the program
        running = False

# check the loop condition
while i <= int(rollInput):
    # assign randomly to diceNum variable (between 1 and 6)
    diceNum = random.randint(1,6)
    # check the condition
    if int(rollInput) in range(0,8+1):
        # print output
        print("Dice " + str(i) + " : " + str(diceNum))
    # calcuale result
    result += diceNum
    # increment the value i
    i += 1
# check the condition
if i == 1:
    # print the result
    print("RESULT: " + str(result))
# check the condition
else:
    # print the result
    print("==========")
    print("RESULT: " + str(result))
    print("==========")
    

