"""
    Description :   You will write a function that take a list in parameters and return a dictionary with the element of the list as key, and the number of occurrences as value. 
    Requirements :  ● Program must be named : 31_dict_count.py and saved into week02/ex folder 
    Hint :  ❖ function 
            ❖ list 
            ❖ dictionary 
            ❖ occurrences 
    Output : 
            dict_count(​[“a, “a”, “a”, “b”, “c”, “d”, “c”, “b”, “c”, “d”, “c”, “e”, “e”, “e”]) 
            >> {a: 3, b: 2, c: 4, d: 2, e: 3} 
"""

# Defining the function/method that take (myList) parameter/augument
def dict_count (myList):
    # inside the function/method
    # print output of (myList) that take from passed list into it
    print("dict_count(" + str(myList) + ")")
    # declare (listItemsCount) variable and to know the number of values of (myList) list with only unique values as a list
    listItemsCount = list([item, myList.count(item)] for item in list(myList))
    # declare (myDict) variable and to assign (listItemsCount) list and sorted as a dictionary. keys=>(myList)_values : values=> (myList)_occurencesOfValues
    myDict = (dict(sorted(listItemsCount)))
    # print output of (myDict).
    print(">> " + str(myDict))
    # return (myDict) dictionary with the element of the list as key, and the number of occurrences as value
    return myDict
# outside the function/method
# call dict_count() function/method with passing list into (myList) parameter/augument
dict_count(['a', 'a', 'a', 'b', 'c', 'd', 'c', 'b', 'c', 'd', 'c', 'e', 'e', 'e'])

