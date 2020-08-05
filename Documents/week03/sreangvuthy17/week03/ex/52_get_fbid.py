"""
    Description :   You will create a function that take one string in argument ( that’s represent a valid a facebook url or fb username and then a tuple with  the request status_code ( usually it will be 200 ) in the first element the associated ID in the second element ) 
                    If no ID is found, you will return a tuple with the status_code as first element and 0 in the second element. 
 
                    The url endpoint is : ​https://findmyfbid.com/  
 
                    The params you have to provide is : {‘url’ : ‘your_fb_url_here’} 
 
                                Your have to make a POST request. 
 
    EXAMPLE: 
            get_fbid(“​https://facebook.com/JohnDoe​”)  ⇒ ​(200, 1213161789) 

            get_fbid(“zuck”)    ⇒ ​(200, 4) 

            get_fbid(“adwopawpodawodpwdpwoawopdwopawopdw”)  ⇒ ​ (200, 0) 
 
    Requirements :  ● Program name : ​52_get_fbid  
                    ● Function name : ​get_fbid 
                    ● Directory : ​week03/ex ​folder 
 
    Hint :  ❖ requests 
            ❖ post

"""

import requests

def get_fbid(facebook_url_username):
    url = "https://findmyfbid.com/"
    params = {"url" : facebook_url_username}
    response = requests.post(url = url, params = params)
    dict_json = response.json()
    my_code_status = response.status_code
 
    try:
        fbid = dict_json.get("id")
        my_tuple = (my_code_status, fbid)   
        print('get_fbid("' + str(facebook_url_username) + '") => ' + str(my_tuple))
    except:
        my_tuple = (my_code_status, 0)
        print('get_fbid("' + str(facebook_url_username) + '") => ' + str(my_tuple))


# get_fbid("https://www.facebook.com/THY.ZEVO")
# get_fbid("zfhtfchkvgjbkbnklinmlknkbkk")

