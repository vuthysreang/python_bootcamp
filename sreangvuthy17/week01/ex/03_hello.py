""" Description :   You will write a program that display “Hello World!” N times inside the console. 
                    The program will first ask you to enter a number (N).  Then, inside a loop, display as many “Hello World!” as specify If no argument is passed, display “Nothing to display” After displaying the result, the program must quit. 
    Requirements :  ● Program must be named : ​03_hello.py​ and saved into​ week01/ex ​folder 
    Hint :  ❖ print function 
        ❖ input function 
        ❖ loop 
"""

# user input
n = input('Enter a number:\n>> ')
# check the condition is digit or not
if n.isdigit():
    # convert string to integer
    x = int(n)
    # assign variable 
    i = 0
    # check loop condition
    while i < x:
        print("Hello World!")
        i += 1
# check the condition if empty return "Nothing to display"
elif n == "":
    print('Nothing to display')


