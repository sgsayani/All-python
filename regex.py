import re


t="I love my mom"
x=re.search("\AI.*mom$", t)
if x:
  print("YES! We have a match!")
else:
  print("No match")