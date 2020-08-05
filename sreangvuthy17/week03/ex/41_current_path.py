"""
    Description :   You will write a function that print the current path of your program folder, then you will return it as a string.  
    Requirements :  ● Program name : ​41_current_path.py 
                    ● Function name : ​current_path 
                    ● Directory : ​week03/ex ​folder 
    Hint :  ❖ os library 
            ❖ os path
"""

import os

def current_path():
    my_current_path = os.getcwd()
    print("My current path of my program folder is:\n>>  " + str(my_current_path))
    return  str(my_current_path)


#current_path()

