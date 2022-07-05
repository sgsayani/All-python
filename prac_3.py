#string
#https://www.w3resource.com/python-exercises/string/

"""
a=str(input("Enter string : "))
b=len(a)
print(b)

"""

"""
a=str(input("enter any sstring"))
all_freq={}

for i in a:
    if i in all_freq:
        all_freq[i] +=1
    else:
        all_freq[i]=1

print(all_freq)

"""


"""
a=str(input("enter string : "))
b={}
for i in a:
    if i in b:
        b[i] +=1
    else:
        b[i] =1
print(b)

"""
a="sayani"
a=list(a)
for i in range(len(a)):
    if(a[i]=='a'):
        a[i]='p'
a=''.join(a)
a=a.replace('p', 'a')
print(a)






