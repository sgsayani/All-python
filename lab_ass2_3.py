#3.	Write a Python program to check any Year taken as input is a Leap Year or not.

a = int(input("Enter any year here : "))
while a > 0:
    #print(a)
    if a % 4 == 0 :
        print(a," is leapyear")
    else:
        print(a," is not leapyear")
    break



