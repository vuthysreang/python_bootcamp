"""
    Description :   You will write a function that return the current date with the following format: YYYY-MM-DD. The return value must be a string.
    Requirements :  ● Program must be named : 34_current_date.py and saved into week02/ex folder 
    Hint :  ❖ function 
            ❖ datetime 
    Output : 
            current_date() 
            >> 2021-06-14
"""

from datetime import datetime

# Define current_date() method/function
def current_date ():
    # inside the function/method
    # print output
    print('current_date()')
    # declare (my_current_date) and to assign current date with only date format: YYYY-MM-DD
    my_current_date = datetime.date(datetime.now())
    # convert date into string format
    my_current_date.strftime("%Y-%M-%D")
    # print output of (my_current_date)
    print(">> " + str(my_current_date))
    # return output of (my_current_date)
    return my_current_date
# outside the function/method
# call the current_date() function/method
current_date()
