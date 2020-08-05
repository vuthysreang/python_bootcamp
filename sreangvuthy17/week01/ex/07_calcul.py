""" Description :   You will write a program that take ask to enter a number and print the total value of all the numbers you did enter. 
                    If you enter nothing, the program will just display the current result. 
                    If you enter exit the program will quit. 
    Requirements :  ● Program must be named : ​07_calcul.py​ and saved into​ week01/ex ​folder 
    Hint :  ❖ print function 
            ❖ arithmetic operators 
            ❖ conditions
"""

# declare boolean variable
program_running = True
# declare integer variable
total = 0
# check loop condition is True or not
while program_running == True:
    # user input
    numInput = input("Enter a number:\n>> ")
    # check the condition
    if numInput == "":
        # print output
        print("TOTAL: " + str(total))
    elif numInput == "exit":
        # quit program
        program_running = False
    # check condition
    elif numInput.isalpha() and numInput != "exit":
        # print output
        print("Wrong input!!\nPlease enter a number.\nIf you want to stop enter exit.")
    # check the condition
    elif numInput.isdigit() == True or int(numInput) < 0:
        # convert string to number or integer
        numInput = int(numInput)
        # calculation
        total = int(total) + numInput
        # print output
        print("TOTAL: " + str(total))
    
        
            
        


    
