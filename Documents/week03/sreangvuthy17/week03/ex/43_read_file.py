"""
    Description :   You will write a function that take a filename as argument (string).            
                    The filename represent the name of the file your program will read.            
                    First you will make sure that the file exist, then you will print the content and finally you will return the value as string. 
                    If the file is not valid ( folder ) or doesn’t exist :  You will print ‘Invalid FILENAME’ Then, you will return an empty string. 
 
    Requirements :  ● Program name :​ 43_read_file.py 
                    ● Function name : ​read_file 
                    ● Directory :​ week03/ex ​folder 
    Hint :  ❖ Make sure your program doesn’t crash if the filename is not valid. 
            ❖ Make sure that after open a file, you close it.
"""

import os

def read_file(filename):
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


#read_file("my_file.txt")
