"""
    Description :   You will create a function that take a string in parameter and remove every HTML content ( everything between ‘<’ and ‘>’ ) You will return  the new formatted string. 
 
                            You need to do it using REGEX only. 
 
    EXAMPLE : 
            regex_html​("<html lang = 'pl' ><body> content of body </body> ... </html>") 
            ⇒ " content of body  ..." 
 
            regex_html​("<h1>hello</h1> <p>hello</p>") 
            ⇒ "hello hello" 
            
            regex_html​("") 
            ⇒ "" 
            
            regex_html​("hello") 
            ⇒ "hello" 
            
            regex_html​("<<><>>><>") 
            ⇒ ">>" 
 
    Requirements :  ● Program name : ​59_regex_html 
                    ● Function name : ​regex_html 
                    ● Directory : ​week03/ex ​folder 

    Hint :  ❖ re 
            ❖ sub

"""

import re

def regex_html(mystr):

    print('regex_html("' + str(mystr) + '")')
    final_str = re.sub(r'<.*?>', '', mystr)
    print('=> "' + str(final_str) + '"')
    return final_str


# regex_html("<html lang = 'pl' ><body> content of body </body> ... </html>")
# regex_html("<<><>>><>")
