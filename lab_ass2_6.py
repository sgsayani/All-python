#. Write a Python program to check whether a number is Palindrome or not.
a = int(input("Enter any number here : "))
temp = a
c = 0
while a > 0:
    b = a % 10 
    c = c*10+b
    a = a//10
if temp == c :
    print("The number is palindrome ")
else:
    print("This is not palindrome.")