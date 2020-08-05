"""
    Description :   You will create a program that will allow to keep log of your messages inside a file. 
                    To do so, you will use the append function ( it’s allow you to add content at the end of an existing file, if the file doesn’t exist, it will be created automatically). 
                    Your function will take one argument in parameter ( filename ) that will be the given name of your log file. 
 
                    Then you will have a loop that will stop ONLY if the user enter ‘EXIT’ 
                    The loop will contain an input that will display: “$: ” 
 
                    Anything (except EXIT) that will be enter by the user, will create a new line inside the file. Also, before the line, the current date and time will be display in this format : [DD-MM-YYYY hh:mm:ss] 
 
    EXAMPLE :   “$: The Week 3 just started” 
                “$: It’s time to eat! I’m hungry” 
                “$: The bootcamp is finish for today! ” 
 
    EXPECTED OUTPUT IN THE FILE :   [03/06/2019 11:00:00] The Week 3 just started 
                                    [03/06/2019 12:00:05] It’s time to eat! I’m hungry 
                                    [03/06/2019 17:00:00] The bootcamp is finish for today! 
 
    The date and time must correspond to the time you wrote the message.  
 
    Requirements :  ● Program name :​ 47_append_file.py  
                    ● Function name : ​append_file 
                    ● Directory: ​week03/ex ​folder
"""

from datetime import datetime
import os

def append_file(filename):
    while True:
        user_input = input('$: ')
        if (user_input.upper() == "EXIT"):
            break
        else:
            current_datetime = datetime.now().strftime("%d/%m/%Y %X")
            f = open(filename, "a")
            f.write("[" + str(current_datetime) + "] " + str(user_input) + "\n")
            f.close()

#append_file("my_newfile.txt")
