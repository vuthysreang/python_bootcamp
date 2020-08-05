"""
    Description :   You will do EXACTLY the same function that you just did ( json_to_tsv ) 
                    but this time, your function will take a .tsv file and return a .json file. 
                    You must create a valid JSON array. 
 
                    The function will take two parameters : First, the name of the (.tsv) file you want to open, then, the file you want to create (.json) 
 
                This file :
                    (image)

                    Will generate : 
                        (image)
                    
                    bc_tsv is available on the Bootcamp Drive Folder. To make your tests,            
                    click on “Download as” and choose Tab-Separated Values ( TSV ) 
 
                    As this exercises is much more easier that the last one, your function should work for EVERY .tsv and return a correct JSON Array. 

                    If the .tsv file doesn’t exist or is not valid : 
                        Your program will return 0 
                        Else, you programm will return 1 
 
    Requirements :  ● Program name :​ 49_tsv_to_json.py 
                    ● Function name : ​tsv_to_json 
                    ● Directory : ​week03/ex ​folder
 """

import json
import csv
import os


def tsv_to_json(tsv_name, json_name):
    modification = 0
    try:
        if os.path.exists(tsv_name):
            with open(tsv_name, "r") as tsv_file:
                tsv_data = csv.DictReader(tsv_file, delimiter = "\t")
                rowlist = list(tsv_data)

            with open(json_name, "w") as json_file:
                json_data = json.dump(rowlist, json_file, indent = 3)
                modification = 1
                return modification
        else:
            print(">> " + str(tsv_name) + " doesn't exist.")
            return modification
        return modification
    except:
        print("Error occurred.")


#tsv_to_json("my_tsv.tsv", "my_new_json.json")
