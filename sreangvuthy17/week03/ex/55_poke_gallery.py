"""
    Description :   You will create a function, that take no argument and generate a HTML file. 
                    
                    Your html will display the 151 pokemons. To be able to do so, for each pokemon you will get the value:  
                    {"img": "​http://www.serebii.net/pokemongo/pokemon/002.png​"} 
 
                    And generate a HTML Images: 
                    <img src="your_url.png" height="100px" width="100px"> 
                    
                    You just have to replace “your_url.png” with the real Pokemon image URL. Finally, use append or write function to save it into ​pokemon.html 

                    If you did this exercises successfully, you can now open ​pokemon.html inside a web browser and you will see something like that :
                    
                                (image on pdf exersises)


    Endpoint​:  https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json 
 
    Your have to make a GET request. 
 
    Requirements :  ● Program name : ​55_poke_gallery 
                    ● Function name : ​poke_gallery 
                    ● Directory : ​week03/ex ​folder

"""
import requests
import os

def poke_gallery():
    html_file = open("pokemon.html", "w")

    url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    req = requests.get(url)
    dict_json = req.json()
    my_list_dict = dict_json['pokemon']
    
    html_code = "<!DOCTYPE html>\n<html>\n\t<header>\n\t<title></title>\n\t</header>\n\n\t<body>\n"
    end_body = "\n\t</body>\n</html>"
    img_script_1 = '\t\t<img src="'
    img_script_2 = '" height="100px" width="100px">\n'

    html_file.write(html_code)
    for pic in my_list_dict:
        html_file.write(img_script_1)
        html_file.write(pic['img'])
        html_file.write(img_script_2)

    html_file.write(end_body)


poke_gallery()
