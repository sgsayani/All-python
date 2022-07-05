#2.	Write a Python program to check given number is Prime or not.

a= int(input("Enter any number here :"))

while a > 0 :
      print(a)
      if a % 2 == 0 :
            print("Number is not prime number.")
      else:
            print("This number is prime number ")
      break
