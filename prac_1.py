#basic part 1
#https://www.w3resource.com/python-exercises/python-basic-exercises.php
import sys
import datetime
print("helloworld")
a="""Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""
print(a)
print(sys.version)

b=float(input("Radious :"))

print(str(3.14*b**2))
now=datetime.datetime.now()
print(now.strftime("%D %H:%M:%S" ))