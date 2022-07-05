#1. Write a Python program to calculate the roots of a quadratic equation.
import math  
# function for finding roots  
def findRoots(a, b, c):  
    p = b * b - 4 * a * c  
    s = math.sqrt(abs(p))  
    if a > 0:  
        print(" real and different roots ")  
        print((-b + s) / (2 * a))  
        print((-b - s) / (2 * a))  
    elif p == 0:  
        print(" real and same roots")  
        print(-b / (2 * a))  
    else:  
        print("Complex Roots")  
        print(- b / (2 * a), " + i", s)  
        print(- b / (2 * a), " - i", s)  
a = int(input("Enter a:"))  
b = int(input("Enter b:"))  
c = int(input("Enter c:"))  
# If a is 0, then incorrect equation  
if a == 0:  
    print("Input correct quadratic equation")  
else:  
    findRoots(a, b, c) 
    
    