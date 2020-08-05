""" Description :   You will write a program that will ask for strings until you enter the command: “Generate”. 
                    Then, for each string, a new line will be generate and display as an HTML paragraph. 
    Requirements : ● Program must be named : ​15_html_text.py​ and saved into​ week01/ex ​folder 
    Hint :  ❖ print function 
            ❖ string 
            ❖ loop 
"""

# list declaration
text = []
# declaration boolean variable
program_running = True
# check the loop condition
while program_running == True:
    # user input
    strInput = input("Enter a string: ")
    # check the condition
    if strInput == "Generate":
        # check loop condition
        for i in text:
            # print output
            print("<p>" + i + "<p>")
        # break the program
        break
    # check other conditions
    else:
        # print text into list
        text.append(strInput)

        
