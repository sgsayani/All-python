

import re 
Name =  input("Enter your name : ")

def isValid(pancard): 
    Result=re.compile("[A-Za-z]{5}\d{4}[A-Za-z]{1}") 
    return Result.match(pancard) 

pancard=input("enter your pancard number")
if (isValid(pancard)):  
    print ("It's a Valid PAN Number")      
else : 
    print ("Invalid PAN Number entered.")