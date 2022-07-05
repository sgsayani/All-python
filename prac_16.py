
#functions

def area(radius):
    area=3.141*(pow(radius,2))
    return area
print(area(2))

def sum(numbers):
    sum=numbers+10
    return sum
print(sum(20))



def sum():
    num=2
    sum=25+num
    return sum
print(sum())


name="sayani"
def names():
    name="sonali"
    return name
print(name)

name ='unknown'
def set_defaults():
    global name
    name ='martin'
set_defaults()
print(name)


def msg(to,text):
    print()


def sayani(string,list,number):
    number = 10
    string='sayani ghatak'
    list=[10,20,30]
    print  ("ss",string,number, list )

number=1
string='hi'
list=[1,2,3,7]

print("before:",number,string,list)

sayani(string, list, number)

print("after :",number,string,list)