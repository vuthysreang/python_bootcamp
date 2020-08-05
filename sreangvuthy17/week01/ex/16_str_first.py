""" Description :   You will write a program that ask for one string as and return the first character. 
                    If no argument is passed, display “Empty” 
    Requirements : ● Program must be named : ​16_str_first.py​ and saved into​ week01/ex ​folder  
    Hint :  ❖ print function 
            ❖ string index 
"""

# user input
strInput = input("Enter a string: ")
# check condition
if strInput == "":
    # print output
    print("Empty")
else:
    # print output
    print(strInput[0])
