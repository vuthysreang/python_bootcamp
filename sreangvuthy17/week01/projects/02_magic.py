""" 
    PROJECT 02: Magic Number Game
"""

import random
# print output
print("Hello, What is your name?")
# user input
nameInput = input()
# print output
print("Well " + nameInput + ", try to guess number I have in mind!")
# generate random number between 1 and 100
randomNum = random.randint(0, 101)
# declaration boolean variable
running = True
# declaration variable
count = 0

# check loop condition
while running == True:
    # icrement count variable
    count += 1
    # user input 
    numInput = input(">> ")
    # check the condition
    if numInput.isdigit() == True:  
        # convert numInput variable into int   
        guessNum = int(numInput)
        # check the condition
        if guessNum > randomNum:
            # print output
            print("Too high, try again!")
        # check condition
        elif guessNum < randomNum:
            # print output
            print("Too low, try again!")
        # check condition
        elif guessNum == randomNum:
            # check nested condition
            if count == 1:
                # print output
                print("You won in 1 turn only, that's amazing!")
            # check the condition
            else:
                # print output
                print("It took you " + str(count) + " turns to guess my number which was " +str(randomNum))
            # print output
            print("Do you want to play again? [Y/N]")
            # declaration boolean variable
            newRunning = True
            # check loop condition
            while newRunning:
                # user input
                agreeInput = input()
                # check condition
                if agreeInput == "N" or agreeInput == "n":
                    # print output
                    print("Ok, bye " + nameInput + "! See you later!")
                    # quit program
                    exit()
                # check the condition
                elif agreeInput == "Y" or agreeInput == "y":
                    # print output
                    print("Hello, What is your name?")
                    # user input
                    nameInput = input()
                    # print output
                    print("Well " + nameInput + ", try to guess number I have in mind!")
                    # Generate random number between 1 and 100
                    randomNum = random.randint(0, 101)
                    # declare count = 0 again to reset the number of turns
                    count = 0
                    # quit while loop
                    newRunning = False
                # check the condition
                else:
                    # print output
                    print("Sorry, I did not understand. Let me repeat:")
                    print("Do you want to play again? [Y/N]")
    # check the condition
    else:
        # print output
        print("Warning!, please enter number between 1 and 100.")
        
                
                
            
