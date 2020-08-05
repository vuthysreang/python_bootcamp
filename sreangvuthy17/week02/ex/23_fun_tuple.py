""" 
    Description :   You will write a function that take 2 parameters and return a Tuple. 
    Requirements :  ● Program must be named :​ 23_fun_tuple.py​ and saved into​ week02/ex ​folder 
    Hint :  ❖ function 
            ❖ tuple   
    Output : 
            fun_tuple(‘abc’, 123) 
            >> (‘abc’, 123)
"""

# Defining the function/method that take 2 parameters (strDisplay, numDisplay)
def fun_tuple(myStr, myNum):
    # inside the function/method
    # print output or return/display the value of parameters (strDisplay, numDisplay)
    print("fun_tuple('" + myStr + "', "  + str(myNum) + ")")
    # put (strDisplay, numDisplay) parameter into tuple
    myTuple = (myStr, myNum)
    myTuple = tuple(myTuple)
    # print output of (myTuple)
    print(">> " + str(myTuple))
    # return output of (myTuple) tuple
    return myTuple

# outside the function/method
# call fun_tuple() function/method with passing 2 values intto the 2 parameters/auguments
fun_tuple('abc', 123)

