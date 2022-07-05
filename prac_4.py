a="restart"
a=list(a)
for i in range(len(a)):
   if(a[i]=='r') :
       a[i]='$'
a=''.join(a)
print(a)
