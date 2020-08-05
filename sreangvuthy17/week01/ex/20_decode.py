""" Description :   Now that you have successfully create your program that can encode a message with ROT13, we will need to create one to decode it. 
                    You will write a program that decode a string with ROT13 system 
    Requirements : ● Program must be named : ​20_decode.py​ and saved into​ week01/ex ​folder 
    Output : 
        $​ python 20_decode.py  
        Enter your encrypted message: Guvf vf n frperg zrffntr. 
        This is a secret message. 
        $​ python 20_decode.py  
        Enter your encrypted message: 
        Nothing to decode.
"""

strInput = input('Enter your encrypted message: ')
strLength = len(strInput)
strOutput = ""

if strInput == "":
    print('Nothing to decode.')

for i in range(strLength):
    asciiChar = ord(strInput[i])

    if strInput[i].isalpha():
        strInputAscii = asciiChar - 13
        if strInput[i].isupper():
            if strInputAscii < 65:
                for i in range(13, 0, -1):
                    if asciiChar == (ord('A')-1):
                        asciiChar = ord('Z')
                    asciiChar -= 1
                strInputAscii = asciiChar
        elif strInput[i].islower():
            if strInputAscii < 97:
                for i in range(13):
                    if asciiChar == (ord('a')-1):
                        asciiChar = ord('z')
                    asciiChar -= 1
                strInputAscii = asciiChar
    else:
        strInputAscii = asciiChar
    
    strOutput = strOutput + chr(strInputAscii)
print(strOutput)
