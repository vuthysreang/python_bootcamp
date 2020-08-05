"""
    Description :   You will write a function that take an integer as parameter that represent a number of second and return a list of time. 
                    For example: if the current time is 04:30:12 and the integer = 3 ==> [04:30:12, 04:30:13, 04:30:14] 
                    If the integer is negative or not valid, you will return an empty list and display​ “Invalid integer.” 
    Requirements :  ● Program must be named :​ 38_time_list.py​ and saved into​ week02/ex ​folder 
    Hint :  ❖ loop 
            ❖ list 
            ❖ function 
            ❖ datetime 
            ❖ sleep 
    Output : 
            time_list(5) 
            >> [‘04:30:12’, ‘04:30:13’, ‘04:30:14’, ‘04:30:15’, ‘04:30:16’] 
            time_list(-2) 
            >> [] 
            >> Invalid integer.
"""

from datetime import datetime
import time

# Defining the function/method that take the (num) parameter/augument
def time_list(num):
    # inside the function/method
    # check the condition
    if num <= 0:
        # print the output of (num)
        print("time_list(" + str(num) + ")")
        # declare empty list
        empty_list = []
        # print output of (empty_list) list
        print(">> " + str(empty_list))
        # Display output: ">> Invalid integer."
        print(">> Invalid integer.")
        # return the empty list
        return empty_list
    # check other condition
    else:
        # print output of (num)
        print("time_list(" + str(num) + ")")
        # declare empty list
        my_list_time = []
        # perform loop condition
        for i in range(num):
            # perform to get time format using time/datetime() methods
            my_time = datetime.time(datetime.now())
            # convert time format into string format
            my_current_time_str = my_time.strftime("%H:%M:%S")
            # put (my_current_time_str) into list one by one
            my_list_time.append(my_current_time_str)
            # waiting or sleep for 1 second
            time.sleep(1)
        # print output of (my_list_time)
        print(">> " + str(my_list_time))
        # return output of (my_list_time)
        return my_list_time

# outside the function/method
# call the time_list() method/function with passing integer into parameter/augument        
time_list(0)
