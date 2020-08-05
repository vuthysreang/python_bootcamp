""" Description :   In this program you will create a function that take 2 parameters in value (A and B) and return the total value. 
                    It will print the result and also the calculation. 
    Requirements : ● Program must be named : ​21_fun_calc.py​ and saved into​ week02/ex ​folder 
    Hint :  ❖ function  
            ❖ return 
    Output : 
            fun_calc(5, 15) 
            >> 20 
            >> 5 + 15 = 20 
"""

a = 5
b = 15
# Defining function/method with take 2 parameters/augument (a, b)
def fun_calc (a, b):
    # inside the function/method
    # print output or display a and b value
    print("fun_calc(" + str(a) + ", " + str(b) + ")")
    # print output of total value and also the calculation
    print(">> " + str(a + b) + "\n>> " + str(a) + " + " + str(b) + " = " + str(a + b))
    # return (a + b) that equal to (total)
    return a + b
    
# outside the function/method
# call fun_calc() function/method with passing values into parameters/auguments
fun_calc(5, 15)


