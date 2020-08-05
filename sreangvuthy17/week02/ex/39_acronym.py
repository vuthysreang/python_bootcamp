"""
    Description :  You will write a function that take a list and return a list with uppercase format. 
                    If the list is empty, your function will return an empty list. 
    Requirements : ● Program must be named :​ 39_acronym.py​ and saved into​ week02/ex ​folder 
    Hint :  ❖ list 
            ❖ string 
            ❖ loop 
    Output : 
            acronym([“world”, “wide”, “web”]) 
            >> [‘W’, ‘W’, ‘W’] 
            acronym([]) 
            >> []
"""

# Defining acronym() function/method that take (my_list) parameter/augument
def acronym(my_list):
        # inside the function/method
        # check the condition
        if my_list == []:
            # print outputof (my_list)
            print("acronym(" + str(my_list) + ")")
            # assing (my_list) list to (empty_list)
            empty_list = my_list
            # print output of (empty_list)
            print(">> " + str(empty_list))
            # return output of (empty_list)
            return empty_list
        # check the other condition
        else:
            # print output of (my_list)
            print("acronym(" + str(my_list) + ")")
            # covert lowercase (my_list) list into uppercase (my_upper_list) list
            my_upper_list =  [item[0].upper() for item in my_list]
            # print output of (my_upper_list)
            print(">> " + str(my_upper_list))
            # return output of (my_upper_list)
            return my_upper_list

# outside the function/method
# call acronym() with passing list into parameter/augument
acronym(['world', 'wide', 'web'])
