"""
    Description :   You will create a function that convert a JSON Array into a TSV File. The JSON file will look like this one: 
                            (image)
                    Once you will convert it, if you open the new created file with excel or google sheets, it will look like this one:
                            (image)
                    The function will take two parameters : First, the name of the (.json) file you want to open, then, the file you want to create (.tsv) 
                        Step 1: make sure that the .json file specify exist and is valid. 
                        Step 2: extract the json array elements content. 
                        Step 3: create a file with .tsv extension 
                        Step 4: add the content and respect the .tsv format  
                    
                    ( every line is separated by ‘\n’ ) 
                    ( every column is separated by a tab : ‘\t’ ) 
                    
                    If the .json file doesn’t exist or is not valid : 
                        Your program will return 0 
                        Else, you programm will return 1 
                    
                    You can test that your .tsv file is valid by open it on google drive Also, you can copy the output and paste it in a google sheet ( it will automatically dispatch the data in the corrects columns. 
                    
                    bc_test.json​ is available on the Bootcamp Drive Folder  
                    
                    For this exercise, your goal is to make it work for this file only. 
                    If you think it’s too easy, you can do the same but that can adapt for any kind of data, you will get bonus! 
 
    Requirements :  ● Program name :​ 48_json_to_tsv.py 
                    ● Function name : ​json_to_tsv  
                    ● Directory: ​week03/ex ​folder

"""

import json
import csv
import os

def json_to_tsv(json_name, tsv_name):
    modification = 0
    try:
        if os.path.exists(json_name):  
            with open(json_name, "r") as json_file:
                json_data = json.load(json_file)

            with open(tsv_name, "w") as tsv_file:
                tsv_data = csv.DictWriter(tsv_file, json_data[0], delimiter='\t')
                tsv_data.writeheader()
                tsv_data.writerows(json_data)
                modification = 1
                return modification
        else:
            print(">> " + str(json_name) + " doesn't exist.")
            return modification

        return modification
    except:
        print("Error occurred.")


#json_to_tsv("my_json.json", "my_tsv.tsv")