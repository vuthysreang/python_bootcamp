"""
    Description :   You will write a function that take a string in parameter that represent a given path and return files path recursively. 
                    The paths must be sorted. If the folder is empty, you must not display it. 
                    Also, don’t display your program name.
        EXAMPLE: 
                (image on pdf exercises)

                60_recursive_folder​(‘.’) 
                ⇒ ['./file_00', './folder_a/file_01', './folder_b/file_02', './folder_c/file_03', './folder_d/file_04'] 

    Requirements :  ● Program name : ​60_recursive_folder.py 
                    ● Function name : ​recursive_folder 
                    ● Directory : ​week03/ex ​folder 
 
    Hint : ❖ os.walk

"""
import os
import fnmatch

def recursive_folder(my_path):
    print('recursive_folder("' + str(my_path) + '")')

    mylist = []
    for root, dir, files in os.walk(my_path):
        for items in fnmatch.filter(files, "*"):
            if not (items == "60_recursive_folder.py"):
                mylist.append(root+"\\"+str(items))
    
    print("=> " + str(mylist))
    return mylist

# recursive_folder(".")
