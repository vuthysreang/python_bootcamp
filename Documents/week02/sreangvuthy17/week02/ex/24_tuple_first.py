"""
    Description :   You will write a function that take a Tuple in parameters and return the first value 
    Requirements :  ● Program must be named : ​24_tuple_first.py and saved into week02/ex folder 
    Hint :  ❖ function 
            ❖ tuple 
    Output : 
            tuple_first((‘abc’, 123)) 
            >> abc 
"""

# Defining the function/method that take (myTuple) parameter/augument
def tuple_first (myTupleFirst):
    # inside the function/method
    # print output or display the (myTuple)
    print("tuple_first(" + str(myTupleFirst) + ")")
    # print output of (myTupleFirst).
    print(">> " + str(myTupleFirst[0]))
    # return the first value of (myTuple) tuple
    return myTupleFirst[0]

# outside the function/method
# call tuple_first() function/method with passing tuple into the (myTupleFirst) parameter/augument
tuple_first(('abc', 123))

