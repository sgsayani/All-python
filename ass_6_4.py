import re
text = "Please contact us at sgsayanighatak@gmail.com for further information."+\
        " You can also contact at sayani28062002.jisu.cse@gmail.com "


emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print (emails)