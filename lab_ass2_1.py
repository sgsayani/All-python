#1. Write a Python program to check whether a number taken by User is Armstrong or not.
# take input from the user
num = int(input("Enter a number: "))

# initialize sum
s = 0

# find the sum of the cube of each digit
a = num

while a > 0:
   digit = a % 10
   s += digit ** 3
   a //= 10

# display the result
if num == s:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
