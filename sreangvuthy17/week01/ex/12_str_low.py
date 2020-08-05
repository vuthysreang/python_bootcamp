""" Description :  You will write a program that will ask for a string and display it lowercase. 
                    If nothing is passed inside the input function, the program will display “The string is empty.” 
    Requirements : ● Program must be named : ​12_str_low.py​ and saved into​ week01/ex ​folder 
    Hint :  ❖ print function 
            ❖ string
"""
# user input
strInput = input("Enter a string: ")
if strInput == "":
    # print output
    print("The string is empty.")
# check other condition
else:
    print(strInput.lower())
