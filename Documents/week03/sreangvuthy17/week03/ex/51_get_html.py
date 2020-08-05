"""
    Description :   You will create a function that take one string in argument that’s represent a valid a url and then return the HTML code of the page as a string. 
                    (No need output for this function but you might need to print your results before submitting your work).  
 
                        You have to make a GET Request. 
 
    Requirements :  ● Program name : ​51_get_html  
                    ● Function name : ​get_html 
                    ● Directory : ​week03/ex ​folder 
 
    Hint :  ❖ requests 
            ❖ get


"""
import requests

def get_html(my_url):
    try:
        html_code = requests.get(my_url) 
        print(html_code.text)   
        return str(html_code)

    except Exception as e:
        print(e)
        return "error"

#get_html("https://www.w3schools.com")
