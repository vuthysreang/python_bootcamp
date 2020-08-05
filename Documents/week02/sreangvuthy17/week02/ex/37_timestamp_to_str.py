"""
    Description :   You will write a function that take a ​timestamp string or integer and convert to readable date and time with the following format: YYYY-MM-DD hh:mm:ss 
                    If the timestamp is not valid, you function will return 0 and display ​“Your timestamp is not valid.”
    Requirements :  ● Program must be named : ​37_timestamp_to_str.py and saved into week02/ex folder 
    Hint :  ❖ function 
            ❖ datetime 
            ❖ timestamp 
    Output : 
            timestamp_to_str(1623646780)  
            >> 2021-06-14 04:59:40 
 
            timestamp_to_str(“1623646780”)  
            >> 2021-06-14 04:59:40 
 
            timestamp_to_str(“abc”) 
            >> Your timestamp is not valid.

                                                        
        NOTE: You can find timestamp on this link: ​https://www.epochconverter.com/
"""

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

# Defining the timestamp_to_str() function/method that take (my_timestamp) parameter/augument
def timestamp_to_str(my_timestamp):
    # inside the function/method
    try:
        # check the condition
        if my_timestamp.isdigit() == False:
            # print output of (my_timestamp)
            print('timestamp_to_str("' + str(my_timestamp) + '")')
            # Display output ">> Your timestamp is not valid."
            print(">> Your timestamp is not valid.")
            # return 0 value to exit program
            return 0
        # check the other condition
        else:
            # convert (my_timestamp) string to (my_timestamp) integer
            my_timestamp = int(my_timestamp)
            # print output of (my_timestamp)
            print('timestamp_to_str("' + str(my_timestamp) + '")')
            # covert timestamp into readable datetime that following the format: YYYY-MM-DD hh:mm:ss
            my_datetime = datetime.fromtimestamp(my_timestamp)
            # print output of (my_datetime)
            print(">> " + str(my_datetime))
            # return output of (my_datetime)
            return my_datetime.strftime("%Y-%M-%D %H:%M:%S")
    except:
        # print output of (my_timestamp)
        print('timestamp_to_str(' + str(my_timestamp) + ')')
        if my_timestamp >= 0:
            # covert timestamp into readable datetime that following the format: YYYY-MM-DD hh:mm:ss
            my_datetime = datetime.fromtimestamp(my_timestamp)
            # print output of (my_datetime)
            print(">> " + str(my_datetime))
            # return output of (my_datetime)
            return my_datetime.strftime("%Y-%M-%D %H:%M:%S")
        else:
            # convert negative timestamp into readable datetime that following the format: YYYY-MM-DD hh:mm:ss
            my_datetime = datetime(1970, 1, 1) + timedelta(seconds = my_timestamp)
            # print output of (my_datetime)
            print(">> " + str(my_datetime))
            # return output of (my_datetime)
            return my_datetime.strftime("%Y-%M-%D %H:%M:%S")


# outside the function/method
# call timestamp_to_str() function/method with passing values into parameter/augument
timestamp_to_str(-2)
timestamp_to_str(0)
timestamp_to_str(1623646780)
timestamp_to_str("1623646780")
timestamp_to_str("abc")

