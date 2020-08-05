""" Description :   You will write a program that take will ask for a number in parameter and display ​“<number> is EVEN” or ​“number is ODD”​. 
                    If the number is not an integer, you will have to display ​“<input> is not a valid number.”​.             
                    If you enter ​“exit” ​or “EXIT” the program will quit. Else the program will continue ask you for a number. 
    Requirements :  ● Program must be named : ​06_odd_even.py​ and saved into​ week01/ex ​folder 
    Hint :  ❖ print function 
            ❖ input function 
            ❖ arithmetic operators ❖ conditions 
"""

# assign the True variable
program_is_running = True
# check the loop True or False
while (program_is_running == True):
    # user input
    n = input("Enter a number:\n>> ")
    # check the condition
    if n == "EXIT" or n == "exit":
        # If program_is_running is False the program will be break
        program_is_running = False
    # check he condition again (check if digit or not)
    elif n.isdigit():
        # convert string to integer or number
        num = int(n)
        # check the condition again (check is even or not)
        if (num % 2 == 0):
            print(n+" is EVEN")
        # check the condition again (check is odd or not)
        else:
            print(n+" is ODD")
    # check the condition again after above "EXIT" or "exit"
    else:
        print(n+" is not a valid number.")




    
