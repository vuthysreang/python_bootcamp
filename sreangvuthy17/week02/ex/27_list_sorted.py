"""
    Description :   You will write a function that take a list in parameters and return a sorted list.
    Requirements : ● Program must be named :​ 27_list_sort.py​ and saved into​ week02/ex ​folder 
    Hint :  ❖ function 
            ❖ list 
            ❖ sort     
    Output :  
            list_sort([4, 2, 19, 50, 49, 48, 1, 2, 3, 4, 5]) 
            >> [1, 2, 2, 3, 4, 4, 5, 19, 48, 49, 50]
"""

# Defing the function/method that take (myList) augument/parameter
def list_sort(myList):
    # inside the function/method
    # print output or display myList
    print("list_sort(" + str(myList) + ")")
    # declare (mySortedList) variable to sort (myList) list
    mySortedList = sorted(myList)
    # print output of (mySortedList) of (myList) list
    print(">> " + str(mySortedList))
    # return a sorted list of (myList) list. Output of (mySortedList)
    return mySortedList
    
# outside the function/method
# call list_set() function/method with passing list into (myList) parameter/augument
list_sort([4, 2, 19, 50, 49, 48, 1, 2, 3, 4, 5])
