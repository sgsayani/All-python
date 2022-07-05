a=int(input("Enter any number : "))
b=int(input("Enter any number : "))
try:
    print("Resorce open ")
    c=a/b
    print(c)
except Exception as a:
    print("this is zerodivision error",a)

finally:
    print("Resourse closed")







