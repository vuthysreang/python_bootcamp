""" Description :   You will write a program that will ask for a string and display it uppercase. 
                    If nothing is passed inside the input function, the program will display “The string is empty.” 
    Requirements :  ● Program must be named : ​11_str_cap.py​ and saved into​ week01/ex ​folder 
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
    print(strInput.upper())
