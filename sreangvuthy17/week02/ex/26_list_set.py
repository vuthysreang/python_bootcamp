"""
    Description :   You will write a function that take a list in parameters and return a List with unique values only. 
    Requirements :  ● Program must be named : ​26_list_set.py​ and saved into​ week02/ex ​folder 
    Hint :  ❖ function 
            ❖ list 
            ❖ set 
    Output : 
            list_set([‘456’, ‘123’, ‘789’, ‘123’, ‘abc’, ‘abc’, ‘def’]) 
            >> [‘456’, ‘123’, ‘789’, ‘abc’, ‘def’]    # It can be get ouput randomly of the list
"""

# Defing the function/method that take (myList) augument/parameter
def list_set (myList):
    # inside the function/method
    # print output or display myList
    print("list_set(" + str(myList) + ")")
    # assign myList into (mySetList) variable to get the unique value of (myList)
    myListUniqueValue = list(set(myList))
    # print output of (myListUniqueValue).
    print(">> " + str(myListUniqueValue))
    # return (myListUniqueValue) that display with only unique value of list
    return myListUniqueValue
    
# outside the function/method
# call list_set() function/method with passing list into (myList) parameter/augument
list_set(["456", "123", "789", "123", "abc", "abc", "def"])



