"""
    Description :   In this program you will create a function take a string and return a list. 
                    The function must split the string at every space character. 
                    If the string is empty you will return an empty list. 
    Requirements : ● Program must be named : ​22_fun_split.py​ and saved into​ week02/ex ​folder 
    Hint :  ❖ Function 
            ❖ list 
            ❖ split 
    Output : 
            fun_split(“Hello! It’s me again!”)
            >> ['Hello!', 'It’s', 'me', 'again!'] 
"""

# Defining function/method that take 1 parametter/augument (myStr)
def fun_split (myStr):
    # inside the function/method
    # print output or display (myStr)
    print('fun_split("' + myStr + '")')
    # split myStr and then put it into list
    strList = list(myStr.split())
    # print output of strList
    print(">> " + str(strList))
    # return strList output
    return strList

# outside the function/method
# call fun_split() function/method with passing string to parameter/augument (myStr)
fun_split("Hello! It's me again!")

