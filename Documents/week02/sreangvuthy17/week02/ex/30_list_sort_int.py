""" 
    Description :   You will write a function that take a List in parameters and return a sorted List with unique values that are valid numbers that are positive only (-2 is not correct). 
                    also the returned list elements must be INTEGER (not string)
    Requirements :  ● Program must be named : ​30_list_sort_int.py and saved into week02/ex folder 
    Hint :  ❖ function 
            ❖ list 
            ❖ sort 
    Output : 
            list_sort_int([“abc”, “4”, “4”, “4”, “4”, “2”, “3”, “dza”, “def”]) 
            >> [2, 3, 4]
"""

# Defining list_sort_str() function/method that take (myList) parameter/augument
def list_sort_int(myList):
    # inside the function/method
    # print output of (myList)
    print("list_sort_int(" + str(myList) + ")")
    # declare (mySortedListUniqueValue) variable to sort (myList) with unique value using set
    mySortedListUniqueValue = sorted(set(myList))
    # remove non numeric items/elements/values of (mySortedListUniqueValue) list that sorted already. Get only numeric values/items/elements of (mySortedListUniqueValue) list
    mySortedListUniqueValueItems = [item for item in mySortedListUniqueValue if item.isdigit()]
    # convert string elements/values/items of (mySortedListUniqueValueItems) list to INTEGER elements/values/items
    mySortedListUniqueValueNewItems = [int(item) for item in mySortedListUniqueValueItems]
    # print output of (mySortedListUniqueValueNewItems)
    print(">> " + str(mySortedListUniqueValueNewItems))
    # return output of (mySortedListUniqueValueItems) list. Display only INTEGER elements of list
    return mySortedListUniqueValueNewItems

# outside the function/method
# call list_sort_int() function/method with passing list into (myList) parameter/augument
list_sort_int(['abc', '4', '4', '4', '-4', '2', '3', 'dza', 'def'])

