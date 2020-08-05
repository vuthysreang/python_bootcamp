"""
    Description :   You will write a function that take a list in parameters and return a sorted list with unique values only. 
    Requirements :  ● Program must be named: ​28_list_sort_set.py and saved into week02/ex folder 
    Hint :  ❖ function 
            ❖ list 
            ❖ sort 
    Output : 
            list_sort_set([4, 2, 19, 50, 49, 48, 1, 2, 3, 4, 5]) 
            >> [1, 2, 3, 4, 5, 19, 48, 49, 50] 
"""
# Defining list_sort_set() function/method that take (myList) parameter/augument
def list_sort_set (myList):
    # inside the function/method
    # print output of (myList)
    print("list_sort_set(" + str(myList) + ")")
    # declare (mySortedListUniqueValue) variable to sort (myList) with unique value using set
    mySortedListUniqueValue = sorted(set(myList))
    # print output of (mySortedListUniqueValue)
    print(">> " + str(mySortedListUniqueValue))
    # return output of (mySortedListUniqueValue)
    return mySortedListUniqueValue

# outside the function/method
# call list_sort_set() function/method with passing list into (myList) parameter/augument
list_sort_set([4, 2, 19, 50, 49, 48, 1, 2, 3, 4, 5])


