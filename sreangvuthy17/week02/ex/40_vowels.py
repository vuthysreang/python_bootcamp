"""
    Description :    You will write a function that take a string and return the number of vowels. 
                     Also it will display the number of vowels, then display a concatenate string with vowels only in lowercase. 
                     Finally display a concatenate string with all the characters that are not vowels in uppercase. 
                     If not vowels are given, you function will return 0 and print “NO VOWELS"
    Requirements :  ● Program must be named : ​40_vowels.py​ and saved into​ week02/ex ​folder 
    Output : 
            vowels(“what is that ?”) 
            3 
            aia 
            WHTSTHT? 
"""

# Defining vowels() that take (my_str) parameter/augument
def vowels(my_str):
   # inside the function/method
   # check condition
   if not (('a' or 'e' or 'i' or 'o' or 'u') in my_str.lower()):
      # print output of (my_str)
      print('vowels("' + my_str + '")')
      # Display output "NO VOWELS"
      print("NO VOWELS")
      # return 0 to exit program
      return 0
   # check other condition
   else:
      # print output of (my_str)
      print('vowels("' + my_str + '")')
      # declaration variables
      count = 0
      vowel = ""
      con = ""
      # check loop condition
      for c in my_str.lower():
         # check condition
         if c != " ":
            # check nested conditions
            if c in ['a', 'e', 'i', 'o', 'u']:
               # count number of vowels
               count+=1
               # concatenate vowels
               vowel = vowel + c
            # check others conditions
            else:
               # concatenate consonants
               con = con + c
      # print output
      print(count)
      print(vowel)
      print(con.upper())
      # return number of vowels that in (my_str)
      return count
      
# outside the function/method
# call vowels() with passing string into parameter/augument
vowels("What is that ?")

