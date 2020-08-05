""" Description :   You will write a program that ask for one string as and return the last character. 
                    If no argument is passed, display “Empty” 
    Requirements :  ● Program must be named : ​17_str_last.py​ and saved into​ week01/ex ​folder  
    Hint :  ❖ print function 
            ❖ string index 
"""

# user input
strInput = input("Enter a string: ")
# check the condition again
if strInput == "":
    # print output
    print("Empty")
else:
    # reverse the strInput
    x = strInput[::-1]
    # print output (we want to print the last character of the string)
    print(x[0])
