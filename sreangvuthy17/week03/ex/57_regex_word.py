"""
    Description :   You will create a function that remove all words from a string length of between 1 and give number. 
                    This function will take one integer in parameter that represent the length and one string that represent the text to be formatted. 
                    You need to return the new string. If the number is negative or 0 you will return an empty string. The special characters will not be removed. 
 
                            You need to do it using REGEX only. 
 
    EXAMPLE : 
            regex_word(3, “My name is Kevin”) 
            ⇒ “name Kevin” 
 
            regex_word(5, “How are you today?”) 
            ⇒ “?” 
 
            regex_word(2, “Is it a cat or is it a dog?”) 
            ⇒ “cat dog?” 
 
    Requirements :  ● Program name : ​57_regex_word  
                    ● Function name : ​regex_word 
                    ● Directory : ​week03/ex ​folder 
 
    Hint :  ❖ re 
            ❖ sub

"""

import re

def regex_word(num, text):
    while True:
        print('regex_word(' + str(num) + ', "' + str(text) + '")')
        if num <= 0:
            empty_str = ""
            return empty_str
        else:
            if isinstance(text, str):
                final_str = re.sub(r"\b\w{1," + str(num) + r"}\W*\b", "", text)
                print("=> " + str(final_str))
                return final_str
            else:
                print("=> " + str(text) + " is not a string.")
                return 0

# regex_word(3, "My name is Kevin")
# regex_word(2, "Is it a cat or is it a dog?")
# regex_word(5, "How are you today?")
# regex_word(2, 123456)
