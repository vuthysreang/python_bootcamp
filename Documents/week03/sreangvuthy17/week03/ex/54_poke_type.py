"""
            (image on pdf exercises)

    Description :   You will create a function that take a string list in parameter and return a list of tuple with two elements: (1. ID, 2. NAME). 
 
                    The string list parameter will represent a Pokemon Type. (for example ‘Fire’, ‘Water’, ‘Psychic’...) 
 
                    To do so, you will make a get request to the endpoint, and find every Pokemon that got the desired type inside the ‘type’ Key (it’s represent a string array). 
 
                    ALL TYPES MUST BE FOUND IN TYPE TO BE ACCEPTED (watch the output) 
                    If no Pokemons are found you will return an empty list: [] 

    Endpoint​:  https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json 
 
                        Your have to make a GET request. 
 
    EXAMPLE: 
            poke_type([‘Psychic’]) 
            ⇒ [(63, 'Abra'), (64, 'Kadabra'), (65, 'Alakazam'), (79, 'Slowpoke'), (80, 'Slowbro'), (96, 'Drowzee'), (97, 'Hypno'), (102, 'Exeggcute'), (103, 'Exeggutor'), (121, 'Starmie'), (122, 'Mr. Mime'), (124, 'Jynx'), (150, 'Mewtwo'), (151, 'Mew')]) 
 
            poke_type([‘Water’, ‘Psychic’]) 
            ⇒ [(79, 'Slowpoke'), (80, 'Slowbro'), (121, 'Starmie')] 
 
            poke_type([‘Water’, ‘Fire’]) 
            ⇒ [] 
 
    Requirements :  ● Program name : ​54_poke_type 
                    ● Function name : ​poke_type 
                    ● Directory : ​week03/ex ​folder

"""

import requests

def poke_type(mylist):
    tuple_list = []
    url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    req = requests.get(url)
    dict_json = req.json()

    my_list_dict = dict_json['pokemon']

    for dic in my_list_dict:
        if set(mylist).issubset(dic['type']):
            tuple_list.append((dic['id'], dic['name']))

    print("=> " + str(tuple_list))
    
    return tuple_list
    

    
# poke_type(["Psychic", "Water"])
# poke_type(['Water', 'Fire'])
