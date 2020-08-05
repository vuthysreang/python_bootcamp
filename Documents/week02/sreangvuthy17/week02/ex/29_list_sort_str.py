"""
    Description :  You will write a function that take a list in parameters and return a sorted list with unique values only with non numeric values. 
    Requirements : ● Program must be named : ​29_list_sort_str.py and saved into week02/ex folder 
    Hint :  ❖ function 
            ❖ list 
            ❖ sort 
    Output : 
        list_sort_str([“abc”, “4”, “2”, “3”, “dza”, “def”]) 
        >> [‘abc’, ‘def’, ‘dza’] 
"""

# Defining list_sort_str() function/method that take (myList) parameter/augument
def list_sort_str(myList):
    # inside the function/method
    # print output of (myList)
    print("list_sort_str(" + str(myList) + ")")
    # declare (mySortedListUniqueValue) variable to sort (myList) with unique value using set
    mySortedListUniqueValue = sorted(set(myList))
    # remove numeric items/elements/values from (mySortedListUniqueValue) list that sorted already. Get only non numeric values/items/elements
    mySortedListUniqueValueNewItems = [item for item in mySortedListUniqueValue if not item.isdigit()]
    # print output of (mySortedListUniqueValueNewItems)
    print(">> " + str(mySortedListUniqueValueNewItems))
    # return output of (mySortedListUniqueValueItems) list. Display only non numeric elements of list
    return mySortedListUniqueValueNewItems

# outside the function/method
# call list_sort_str() function/method with passing list into (myList) parameter/augument
list_sort_str(['abc', '4', '2', '3', 'dza', 'def'])

