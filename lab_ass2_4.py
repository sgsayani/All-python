#. Write a Python program to calculate sum of n natural numbers.
a = int(input("Enter number here : "))

if a < 0:
    print("Please enter positive number.")
else:
    sum = 0
    while a > 0 :
        sum += a
        a -=1
    print("Sum is : ",sum)





