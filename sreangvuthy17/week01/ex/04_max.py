""" Description :   The program will ask for a number: “Enter a number:” 
                    Then ask for another one: “Enter a second number:” 
                    Finally, the program will display the output. 
                    “Result : BIGGER_NUMBER > SMALLER_NUMBER” 
                    If the numbers are equals: 
                    “Result : NUMBER_01 == NUMBER_02” 
    Requirements :  ● Program must be named : ​04_max.py​ and saved into​ week01/ex ​folder 
    Hint :  ❖ print function 
            ❖ arithmetic operators 
            ❖ conditions
""" 

# user input the first number
num1 = input('Enter a number:\n>> ')
# user input the second number
num2 = input('Enter a second number:\n>> ')
# check condition that the first the second number is digit or not
if num1.isdigit() and num2.isdigit():
    # convert string to number or integer
    x1 = int(num1)
    x2 = int(num2)
    # check the condition
    if x1 < x2:
        print("Result: " + num2 + " > " + num1)
    # check the condition
    elif x1 == x2:
        print("Result: " + num2 + " == " + num1)