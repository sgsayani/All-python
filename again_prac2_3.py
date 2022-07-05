a= int(input("enter any number here:"))
sum=0
num=a

while num>0:
    d=num%10
    sum+=d**3
    num//=10
if a==sum:
    print("amsrtong")
else:
    print("not")