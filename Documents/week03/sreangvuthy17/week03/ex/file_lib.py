"""
    Description :   You will create a Class that will contains useful functions that you just created. 
                    You class will be call FileLib and will contains the following functions:  
 
                    - inspect(self) 
                    - current_path(self) 
                    - read(self, filename) 
                    - write(self, filename, content) 
                    - append(self, filename, content) 
                    - remove(self, filename) 
                    - create_folder(self, folder_list) 
 
                    They must work exactly as the exercises you did previously without the confirmations inpu​t. 
                    Also, don’t mind about self, this is a mandatory convention for every functions created in a Class ( we call them methods ) 
 
                    If you class work you will be able to call the methods this way: 
                        FileLib().inspect() 
                        FileLib().current_path() 
                        FileLib().read(“my_file.txt”) 
                        FileLib().write(“my_file.txt”, “Hello World!”)
                        ...
    Requirements :  ● Program name : ​file_lib.py 
                    ● Class name : ​FileLib 
                    ● Directory :​ week03/ex ​folder 

                    ● Don’t use number (50_file_lib.py) for this file, else you won’t be able to import it as a module. 
""" 

import os
from datetime import datetime
from datetime import date
from datetime import time
import shutil

class FileLib:

    def inspect(self):
        if self == '':
            my_list = []
            print(">> " + str(my_list))
            return my_list
        else:
            file_list = []
            folder_list = []

            for f in os.listdir(self):
                if os.path.isdir(os.path.join(self, f)):
                    folder_list.append((f, 'Folder'))
                    for f1 in os.listdir(os.path.join(self, f)):
                        if os.path.isdir(os.path.join(os.path.join(self, f), f1)):
                            folder_list.append((f1, 'Folder'))
                        else:
                            file_list.append((f1, 'File'))
                else:
                    file_list.append((f, 'File'))

            final_list = list(folder_list + file_list)
            print(">> " + str(final_list))
            return final_list

        def current_path(self):
            my_current_path = os.getcwd()
            print("My current path of my program folder is:\n>>  " + str(my_current_path))
            return str(my_current_path)

    def read(self, filename):
        try:

            if (os.path.exists(filename) and os.path.isfile(filename)):
                f = open(filename, "r")
                readfile = f.read()
                print(str(readfile))
                f.close()
                return str(readfile)

            elif (os.path.exists(filename) == False or os.path.isdir(filename)):
                print(">> Invalid FILENAME")
                emptystr = ""
                return emptystr

            else:
                print("Something wrong!")

        except:
            print("Error occurred!")


    def write(self, filename, content):
        if os.path.exists(filename) == False:
            f = open(filename, "x")
            f.write(content)
            f.close()
            return 1
        elif os.path.exists(filename):
            running = True
            while running:
                user_input = input("Are you sure you want to replace " + str(filename) + "? [Y/N]\n>> ")
                if (user_input == "Y" or user_input == "y"):
                    os.remove(filename)
                    f = open(filename, "x") 
                    f.close()
                    return 1
                elif (user_input == "N" or user_input == "n"):
                    return 0
                else:
                    print(">> Invalid Option")

    def append(self, filename):
        while True:
            user_input = input('$: ')
            if (user_input.upper() == "EXIT"):
                break
            else:
                current_datetime = datetime.now().strftime("%d/%m/%Y %X")
                f = open(filename, "a")
                f.write("[" + str(current_datetime) + "] " +
                        str(user_input) + "\n")
                f.close()

    def remove(self, filename):
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

    def create_folder(self, folder_list):
        modification = 0
        if folder_list == []:
            return 0

        for foldername in folder_list:
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


