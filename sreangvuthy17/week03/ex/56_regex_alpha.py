"""
    Description :   You will create a function that detect if string contains only value from a-z A-Z and 0-9.  
 
                    You function will take one argument in parameter ( a string ) and will return True or False ( boolean ) 
 
                    If the string in empty, you will return False. 
 
                            You need to do it using REGEX only. 
 
    Example : 
            regex_alpha(“abc123”) 
            ⇒ True  
 
            regex_alpha(“AAA123”) 
            ⇒ True  
 
            regex_alpha(“abc123!”) 
            ⇒ False 
 
            regex_alpha(“”) 
            => False 
 
    Requirements :  ● Program name : ​56_regex_alpha 
                    ● Function name : ​regex_alpha 
                    ● Directory : ​week03/ex ​folder 
 
    Hint :  ❖ re

"""

import re

def regex_alpha(mystr):
    if mystr == "":
        print('regex_alpha("' + str(mystr) + '")')
        print("=> False")
        return False
    else:
        # if re.match("^[a-zA-Z0-9]*$", mystr): we can use this all so. 
        
        if re.findall("^[a-zA-Z0-9]*$", mystr):
            print('regex_alpha("' + str(mystr) + '")')
            print("=> True")
            return True
        else:
            print('regex_alpha("' + str(mystr) + '")')
            print("=> False")
            return False


# regex_alpha("abc123!!@@#")
# regex_alpha("ABCKJI1232")
# regex_alpha("AbcdE123s")
# regex_alpha("")
