""" Description :   You will write a program that ask for a string and display the length. 
                    If nothing is passed inside the input function, the program will display “The string is empty.” 
    Requirements :  ● Program must be named : ​10_str_length.py and saved into week01/ex folder 
    Hint :  ❖ print function 
            ❖ string 
            ❖ len
"""

# user input
strInput = input("Enter a string:\n>> ")
# check the condition
if strInput == "":
    # print output
    print("The string is empty.")
# check other condition
else:
    # print output
    print(len(strInput))
