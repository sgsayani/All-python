
#basic parrt 1

"""a=int(input("Enter name :"))
b=int(input("Enter title:"))
a=(a+b)
b=(a-b)
a=(a-b)
print(a)
print(b)"""



"""a=(input("enter values"))
list=a.split(",")
tuple=tuple(list)

print(list)
print(tuple)"""


"""
filename=input("enter file name")
f_extns=filename.split(".")
print(repr(f_extns[-1]))
"""


"""color=["Red","Green","pink","yellow"]
print(color)
color.append("blue")
print(color)
print(color[0],color[3])"""

"""

exam_date=(11,12,2014)
print("%i/%i/%i"%exam_date)"""

"""
a=int(input("Enter the value "))
a1=int("%s" %a)
a2=int("%s%s" %(a,a))
a3=int("%s%s%s" %(a,a,a))
p=a1+a2+a3

print(p)"""


#print(abs.__doc__)



"""import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
print(c.formatyear(2022))
"""
"""
from datetime import date
a=date(2014,7,2)
b=date(2014,7,11)
c=b-a
print(c.days)"""

"""
r=int(input("enter the radious : "))
v=(4/3)*3.12*r*r*r
print(v)"""

"""
a=int(input("enter value :"))
if(a>17):
    print((a-17)*2)
    
else:
    print((a-17))

"""
"""
a=int(input("1st value : "))
b=int(input("2nd value : "))
c=int(input("3rd value : "))
sum=a+b+c
if a == b == c :
    print(sum*3)
else:
    print(sum)
    """

def string(str,n):
    result=""
    for i in range(n):
        retult= result + str 
    return result
print(string('sayani', 2))
print(string('.py', 8))
    






