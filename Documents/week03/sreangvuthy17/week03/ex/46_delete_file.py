"""
    Description :   You will create a function that has the power to delete any file or any folder that is specify. 
                    Your function will take one parameter (filename) that can be a Folder or a File. 
                    Then, the function will ask for confirmation: 
 
                    “Are you sure you want to delete <FILENAME>? [Y/N]” 
                    If the user write anything that is not Y or N you will print: 
                        “Invalid Option” and then print the confirmation message again:  
                        “Are you sure you want to delete <FILENAME>? [Y/N]” 
                    If a file has been deleted, your function will return 1, else return 0. 
 
            Be careful with this program and don’t delete your work! 
 
    Requirements :  ● Program name : ​46_delete_file.py 
                    ● Function name : ​delete_file  
                    ● Directory : ​week03/ex ​folder
"""

import os
import shutil

def delete_file(filename):
    modification = 0
    if os.path.exists(filename):
        while True:
            user_input = input("Are you sure you want to delete " + str(filename) + "? [Y/N]\n>> ")
            if (user_input == "Y" or user_input == "y"):
                if (os.path.exists(filename) and os.path.isfile(filename)):
                    os.remove(filename)
                    modification = 1
                    return modification
                elif (os.path.exists(filename) and os.path.isdir(filename)):
                    shutil.rmtree(filename)
                    modification = 1
                    return modification
            elif (user_input == "N" or user_input == "n"):
                modification = 0
                return modification
            else:
                print(">> Invalid Option")
    else:
        print(">> Sorry! This name doesn't exist to delete.")
    return modification


#delete_file("myfolder")
