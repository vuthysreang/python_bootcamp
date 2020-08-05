"""
    Description :   You will write a function that take a List in parameters and return a list of tuples with the element of the List as Key, and the number of occurrences as value. ​
                    The list output must be sorted by key​. Then the function will display the sum of all the items. 
                    If the list is empty you will return an empty list and display ​“Your string is empty.”​.
                    Before returning the value you will also print the TOTAL. 
    Requirements :  ● Program must be named : 33_dict_count3.py and saved into week02/ex folder 
    Hint :  ❖ Function 
            ❖ list 
            ❖ dictionary 
            ❖ Occurrences 
            ❖ values 
    Output : 
        dict_count3([“a”, “b”, “b”, “c”, “c”, “c”, “c”, “d”, “d”, “e”, “e”, “e”]) 
        >> [(‘a’, 1), (‘b’, 2), (‘c’, 4), (‘d’, 2), (‘e’, 3)] 
        >> TOTAL: 12
"""

# Defining dict_count3() that take (myList) parameter/augument
def dict_count3(myList):
    # inside the function/method
    # check the condition
    if myList == []:
        # assign (myList) equal to (emptyList)
        emptyList = myList
        # return (emptyList)
        print(">> " + str(emptyList) + "\n>> Your string is empty.")
        return emptyList
    # check other condition
    else:
        # find the total number of items of (myList)
        totalListItems = len(myList)
        # print output of (myList)
        print("dict_count2(" + str(myList) + ")")
        # assign (myList) list into (mySet) set
        mySet = set(myList)
        # declare (listItemsCount) variable and to find the number of elements that occur (myList) list with unique values
        listItemsCount = list([item, myList.count(item)] for item in set(mySet))
        # declare (originalListOfTuple) varialbe and to assign list of tuple into (originalListOfTuple)
        originalListOfTuple = [tuple(item) for item in listItemsCount]
        # sort list of tuple by key
        sortedListOfTuple = sorted(originalListOfTuple)
        # print output of (sortedListOfTuple)
        print(">> " + str(sortedListOfTuple))
        # print output of (totalListItems)
        print(">> TOTAL: " + str(totalListItems))
        # return output of (sortedListOfTuple)
        return sortedListOfTuple

# outside the function/method
# call dict_count3() with passing list into (myList) parameter/augument
dict_count3(['a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'e', 'e', 'e'])
