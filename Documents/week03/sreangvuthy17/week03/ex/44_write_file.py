"""
    Description :   You will write a function that take two arguments: The first argument is a filename, the second is the content. 
                    Your program will create a new file inside the current directory with the name you specify. 
                    Then it will write the content you specify in the second argument. 
                    Finally your program will close the file and return 1 
                    
                    If you try to replace a file that already exist, you will ask confirmation of the user :  
                    “Are you sure you want to replace <FILENAME>? [Y/N]” 
                        If the user write Y, you will create the new file and return 1 
                        If the user write N, you will just return 0 
                        If the user write anything else, you will print : 
                            “Invalid Option” and then print the confirmation message again:  
                            “Are you sure you want to replace <FILENAME>? [Y/N]” 
                    
                    Be careful with this program and don’t delete your work! 
    
    Requirements :  ● Program name : ​44_write_file.py 
                    ● Function name : ​write_file 
                    ● Directory :​ week03/ex ​folder
"""
import os

def write_file(filename, content):
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
    

#write_file("my_newfile.txt", "Hello, This is my content.")
