"""
    Description :   You will write a function that return the current date and time with the following format: YYYY-MM-DD hh:mm:ss  
                    The return value must be a string. 
    Requirements :  ● Program must be named :​ 36_date_time.py​ and saved into​ week02/ex ​folder 
    Hint :  ❖ function 
            ❖ datetime 
    Output : 
            date_time() 
            >> 2021-06-14 04:59:40
"""

from datetime import datetime
from datetime import time
from datetime import date
# Define date_time() method/function
def date_time():
    # inside the function/method
    # print output
    print('date_time()')
    # declare (my_current_datetime) and to assign current datetime with datetime format: YYYY-MM-DD hh:mm:ss
    my_current_datetime = datetime.now()
    my_current_datetime.strftime("%Y-%M-%D %H:%M:%S")
    # print output of (my_current_datetime)
    print(">> " + str(my_current_datetime))
    # return output of (my_current_datetime)
    return my_current_datetime

# outside the function/method
# call the date_time() function/method
date_time()
