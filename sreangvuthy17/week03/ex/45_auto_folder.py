"""
    Description :   You will create a program that take a list of string as argument, that represents folders names. 
                    Then, for each, you will create a folder with the corresponding name. 
                    Before create anything, you will check that the folders doesn’t already exists. 
                    If they, you will ask:  “Are you sure you want to replace <FOLDER_NAME>? [Y/N]” 
                        If the user enter anything that is not Y or N, you will write: 
                            “Invalid Option” and then print the confirmation message again: 
                            “Are you sure you want to replace <FOLDER_NAME>? [Y/N]” 
 
        Make sure that you ask for EVERY folders that already exist only. 
        Be careful with this program and don’t delete your work!
        
        At the end, if your program did create any new folder you will return 1 Else you will return 0. 
        If the list of folder name is empty, your program will also return 0. 
 
    Requirements :  ● Program name :​ 45_auto_folder.py 
                    ● Function name : ​auto_folder 
                    ● Directory :​ week03/ex ​folder 
    
    Hint : ❖ os library
"""

import os
import shutil

def auto_folder(mylist_folder):
    modification = 0
    if mylist_folder == []:
        return 0

    for foldername in mylist_folder:
        if not os.path.exists(foldername):
            os.makedirs(foldername)
            modification = 1
        elif os.path.exists(foldername):
            while True:
                user_input = input("Are you sure you want to replace " + str(foldername) + "? [Y/N]\n>> ")
                if (user_input == "Y" or user_input == "y"):
                    shutil.rmtree(foldername)
                    os.makedirs(foldername)
                    modification = 1
                    break
                elif (user_input == "N" or user_input == "n"):
                    break
                else:
                    print(">> Invalid Option")
    return modification   


#auto_folder(["new_folder_name", "second_folder", "third_folder"])
#auto_folder([])
