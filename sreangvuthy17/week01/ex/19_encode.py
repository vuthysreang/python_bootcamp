""" Description :   ROT13 ("​rotate by 13 places​", sometimes hyphenated ​ROT-13​) is a simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet. 
                    ROT13 is a special case of the Caesar cipher which was developed in ancient Rome. 
                    You will write a program that encode a string with ROT13 system 
    Requirements : ● Program must be named : ​19_encode.py​ and saved into​ week01/ex ​folder 
    Output : 
            $​ python 19_encode.py 
            Enter your secret message: This is a secret message. 
            Guvf vf n frperg zrffntr.  
            $​ python 19_encode.py  
            Enter your secret message:
            Nothing to encode. 
"""

strInput = input('Enter your secret message: ')
strLength = len(strInput)
strOutput = ""

if strInput == "":
    print('Nothing to encode.')

for i in range(strLength):
    asciiChar = ord(strInput[i])

    if strInput[i].isalpha():
        strInputAscii = asciiChar + 13
        if strInput[i].isupper():
            if strInputAscii > 90:
                for i in range(13):
                    if asciiChar == (ord('Z')+1):
                        asciiChar = ord('A')
                    asciiChar += 1
                strInputAscii = asciiChar
        elif strInput[i].islower():
            if strInputAscii > 122:
                for i in range(13):
                    if asciiChar == (ord('z')+1):
                        asciiChar = ord('a')
                    asciiChar += 1
                strInputAscii = asciiChar
    else:
        strInputAscii = asciiChar

    strOutput = strOutput + chr(strInputAscii)
print(strOutput)
