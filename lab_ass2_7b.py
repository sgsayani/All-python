#2nd pattern
a = int(input("Enter any number for draw the pattern  : "))
while a >0 :
 for i in range(a+1,0,-1):
    for j in range(0,i-1):
        print("* ",end=" ")
    print()
 break



