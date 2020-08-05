"""
                                            PROJECT 04 : Top Words 
 
    Description :   For this project, you will write a function, that take a string (text) as parameter and will return the top 3 most occuring words in a list. 
                    Some words like (aren’t) contains characters and must be handle by your function. 
                    The punctuations mark and special characters must not be taking in consideration, you must remove them (example: Hello! will become hello). 
                    Finally, if there are not enough unique words to generate top3 you will generate top2 or top1. If the text is empty you will return an empty list. 
    Requirements :  ● Program must be named : ​04_top_words.py​ and saved into​ week02/projects 
                    ● Your function must be called ​top_words(text)   
                    ● Your function must be case-insensitive and your result have to be lowercase (“Hello, hello, Hello!”) ⇒ “hello” (3 times) 
                    ● If you have more than 3 words that occurs equally, you will have to return a list that respect the order of the first occurrences. 
                    Example:    “hi hello hi wow wow hello good good ” 
                                will return: ==> [“hi”, “hello”, “wow”] 
                                because ‘hi’ ‘hello’ and ‘wow’ are the first 3 words to appears in the text ( even if ‘good’ appears also 2 times )  
    Hint :  ❖ Review your week 01 and week 02 exercises, they might help you :) 
            ❖ Generate your own texts and make a LOT of test before submission! 
            ❖ Take time to read the description / requirements and output AGAIN 
    Output : 
            top_words(“Welcome to Kirirom: Kirirom Institute of Technology and Kirirom National Parc. To contact us, send a message to us!” 
            >> [“to”, “kirirom”, “us”]  
            top_words(“//can’t cant Cant can’t”) 
            >> [“can’t”, ‘cant’] 
            top_words(“hello hello Hello”) 
            >> [“hello”] 
            top_words(“. ??? // ####### // // ???”) 
            >> [] 
            top_words(“”) 
            >> []
"""

# Defining top_words() function/method that take (my_str) parameter/augument
def top_words(my_str):
    # inside the function/method
    # check the condition
    if my_str == "":
        empty_list = []
        print('top_words("' + my_str + '")')
        print(">> " + str(empty_list))
        return empty_list
    # check other conditions
    else:
        # print output of (my_str)
        print('top_words("' + my_str + '")')
        # convert (my_str) to lower case
        my_str = my_str.lower()
        # split (my_str) like a list
        my_list = my_str.split()
        # check and remove secial characters except '
        my_list = [line.strip(" !$%&'()*+,-#./:;<=>?@[\]^_`{|}~") for line in my_list]
        # check loop condition
        while '' in my_list:
            # remove null values of (my_list)
            my_list.remove('')
        # count number of items of list occurs
        my_list_tuple = [(item, my_list.count(item)) for item in my_list]
        # convert list of tuple into dictionary
        my_dict = dict(my_list_tuple)
        # perform to get (my_final_list) is that the list only has top three values
        my_final_list = sorted(my_dict, key = my_dict.get, reverse = True)[:3]
        # print output of (my_final_list)
        print(">> " + str(my_final_list))
        # return output of (my_final_list)
        return my_final_list

# outside the function/method
top_words("Welcome to Kirirom: Kirirom Institute of Technology and Kirirom National Parc. To contact us, send a message to us!")
top_words("hi hello hi wow wow hello good good")
top_words("hello hello Hello")
top_words("//can’t cant Cant can’t")
top_words(". ??? // ####### // // ???")
top_words("")

