"""
    Description :   You will write a function that return a tuple list with all files and folders inside the current path. 
                    For each tuple, the first value will be the file or folder name. 
                    The second value will be the kind of file (‘Folder’ or ‘File’). 
    EXAMPLE : 
            If the current folder path contain 3 FOLDERS ( folder_01, folder_02 and folder_3 ) and 2 FILES ( file_01, file_02 ) 

            The program will return : [(‘folder_01’,’Folder’),(‘folder_02’,’Folder’),(‘folder_03’,’Folder’),( ‘file_01’,’File’),(‘file_02’,’File’)] 
            You must first return all the folders, sorted alphabetically and then the files sorted alphabetically as well. 
            Your program will not return the name of this program.  
            
            If not folders / files found, you will return an empty list.  
            The program will return : [] 
    
    Requirements :  ● Program name :​ 42_current_folder.py  
                    ● Function name : ​current_folder  
                    ● Directory :​ week03/ex ​folder 
 
    Hint :  ❖ os library  
            ❖ os.path
"""

import os

def current_folder(dir_name):

    if dir_name == '':
        my_list = []
        print(">> " + str(my_list))
        return my_list
    else:
        file_list = []
        folder_list = []

        for f in os.listdir(dir_name):
            if os.path.isdir(os.path.join(dir_name, f)):
                folder_list.append((f,'Folder'))
                for f1 in os.listdir(os.path.join(dir_name, f)):
                    if os.path.isdir(os.path.join(os.path.join(dir_name, f), f1)):
                        folder_list.append((f1, 'Folder'))
                    else:
                        file_list.append((f1, 'File'))
            else:
                file_list.append((f, 'File'))
                
        final_list = list(folder_list + file_list)
        print(">> " + str(final_list))

        return final_list


# current_folder("")
# current_folder("D:\PYTHON_BOOTCAMP-KIT\python_bootcamp\sreangvuthy17\week03")

