"""
    Description :  You will write a function that return the current time with the following format: hh:mm:ss  The return value must be a string. 
    Requirements : ● Program must be named : 35_current_time.py and saved into week02/ex folder 
    Hint :  ❖ function 
            ❖ datetime  
    Output : 
            current_time() 
            >> 04:59:40
"""

from datetime import datetime
from datetime import time
from datetime import date
# Define current_time() method/function
def current_time():
    # inside the function/method
    # print output
    print('current_time()')
    # declare (my_current_time) and to assign current time with only time format: hh:mm:ss
    my_current_time = datetime.time(datetime.now())
    # convert time format into string format
    my_current_time = my_current_time.strftime("%H:%M:%S")
    # print output of (my_current_time)
    print(">> " + str(my_current_time))
    # return output of (my_current_time)
    return my_current_time

# outside the function/method
# call the current_time() function/method
current_time()
