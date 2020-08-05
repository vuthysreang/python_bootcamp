"""
    Description :   You will write a function that take a Tuple in parameters and return the second value 
    Requirements : ● Program must be named : ​25_tuple_second.py and saved into week02/ex folder
    Hint :  ❖ function 
            ❖ tuple 
    Output : 
            tuple_second((‘abc’, 123)) 
            >> 123
"""

# Defining the function/method that take (myTuple) parameter/augument
def tuple_second (myTupleSecond):
    # inside the function/method
    # print output or display the (myTuple)
    print("tuple_second(" + str(myTupleSecond) + ")")

    # print output of (myTupleSecond)
    print(">> " + str(myTupleSecond[1]))
    # return secondValue of (myTuple) tuple
    return myTupleSecond[1]

# outside the function/method
# call tuple_second() function/method with passing tuple into the (myTuple) parameter/augument
secondValue = tuple_second(('abc', 123))

