ini_string = 'university'
 
# Character to find
a = "u"
# printing initial string and character
print ("initial string is  : ", ini_string, "\ncharacter to find : ", a)
abc = None
for i in range(0, len(ini_string)):
    if ini_string[i] == a:
        abc = i + 1
        break
     
if abc == None:
    print ("No such character available in string")
else:
    print ("Character {} is present at {}".format(a, str(abc)))
    
    