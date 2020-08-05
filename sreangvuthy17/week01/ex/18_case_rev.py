""" Description :   You will write a program that will ask for a string and replace lowercase with uppercase and uppercase with lowercase. 
                    If not argument is passed, display “Empty” 
    Requirements :  ● Program must be named : ​18_case_rev.py​ and saved into​ week01/ex ​folder  
    Hint :  ❖ string  
            ❖ ascii 
"""

# user input
strInput = input("Enter a string: ")
# check condition
if strInput == "":
    # print output
    print("Empty")
# check condition    
elif strInput.isdigit() == False:
    # swap uppercase to lowercase and swap lower case to uppercase and then print output
    print(strInput.swapcase())
# check other condition
else:
    print("Can not swapcase!!")
