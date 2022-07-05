import re

#split
#string="Hello sayani Ghatak"
#print((re.split(r'\s', string)))

#match
list=['get','give','selenium']

for element in list:
    z=re.match("(g\w+)\W(g\w+)", element)
    
    if z:
        print((z.groups()))



