#Write a Python program to find largest number between three numbers.


a=int(input("Enter 1st number(a) :"))
b=int(input("Enter 2nd number(b) :"))
c=int(input("Enter 3rd number(c) :"))
if a>b and c<a:
    print("a is the largest number ")
elif b>a and b>c:
    print("b is the largest number ")
else:
    print("c is the largest number ")
