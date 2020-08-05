"""
    Description :   You need to create a function that take a string in parameters and return a string without any parenthesis content. 
 
                            You need to do it using REGEX only. 
 
    EXAMPLE: 
            regex_par("(hello) Welcome to KIT (Kirirom Institute of Technology)!" 
            ⇒ " Welcome to KIT !" 
 
            regex_par("((not ok)) )ok( )))(not_ok)(((ok") 
            ⇒ ") )ok))(((ok" 
 
    Requirements :  ● Program name : ​58_regex_par 
                    ● Function name : ​regex_par 
                    ● Directory : ​week03/ex ​folder 
 
    Hint :  ❖ re 
            ❖ sub

"""

import re

def regex_par(mystr):

    print('regex_par("' + str(mystr) + '")')
    final_str = re.sub(r'\([^)]*\)', '', mystr)
    print('=> "' + str(final_str) + '"')
    return final_str


# regex_par("(Hello) Welcome to kIT (Kirirom Institute of Technology)!")
# regex_par("")
# regex_par("((not ok)) )ok( )))(not_ok)(((ok")
