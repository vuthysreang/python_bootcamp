"""
    Description :   You will create a function, that will take one string list as parameters and return a list of tuple. 
                    Each string element of the list  represent a currency pair: ​"EURUSD"​, ​"EURGBP"​, ​"GBPUSD"​, ​"USDJPY"​... 
 
                    For each pair you have inside your array, you will add one element in your tuple list : 
 
                        1. Pair name (example EURUSD) 
                        2. Rate (example 0.549013) 
                        3. Timestamp (example 1558650441)  
                        4. Readable datetime string (example: 14/06/2019 14:33:25) 
 
                    The first three element are found inside the JSON that is return from the API, the last element (datetime string) must be generate by your program using the given timestamp) 
 
                    The url endpoint is :   https://www.freeforexapi.com/api/live  
                    The params you have to provide is : {‘pairs’ : ‘PAIR,PAIR2,PAIR3’} 
                    
                            Your have to make a POST request. 
 
    EXAMPLE : 
            get_currency(‘EURUSD’,’EURGBP’, ‘USDGBP’) 
            ⇒ [('EURUSD', 1.123501, 1559650745, ‘06/04/2019 00:19’), ('EURGBP', 0.886762, 1559650745, ‘06/04/2019 00:19’), ('USDGBP', 0.789285, 1559650745, ‘06/04/2019 00:19’)] 
 
            get_currency(‘ABCDEF’): 
            ⇒ ‘The currency pair 'ABCDEF' was not recognised or supported’ 
 
                Documentation : ​https://www.freeforexapi.com/Home/Api

    Requirements :  ● Program name : ​53_get_currency 
                    ● Function name : ​get_currency 
                    ● Directory : ​week03/ex ​folder 
 
    Hint :  ❖ requests 
            ❖ post 

"""
import requests
from datetime import datetime

def get_currency(mylist):
    mylist_tuple = []
    for str_pairs in mylist:
        url = "https://www.freeforexapi.com/api/live"
        params = {"pairs" : str_pairs}
        response = requests.post(url = url, params = params)
        dict_json = response.json()
        
        if dict_json['code'] == 200:
            my_rates = dict_json['rates'][str_pairs]['rate']
            my_timestamp = dict_json['rates'][str_pairs]['timestamp']
            my_datetime = datetime.fromtimestamp(my_timestamp).strftime("%d/%m/%Y %X")
            
            mylist_tuple.append((str_pairs, my_rates, my_timestamp, my_datetime))
        else:
            print("=> " + str(dict_json['message']))
            
    print("====================================================================================")
    if mylist_tuple == []:       
        return 0
    else:
        print("=> " + str(mylist_tuple))
        return mylist_tuple


#get_currency(['EURUSD', 'EURGBP', 'USDGBP'])
#get_currency(["ABCDEF", 'EURUSD', "ABCDEF", "ABCDEF",'GIHKHILJHHKHKUHKH'])
#get_currency(["ABCDEF"])
