#Python program to swap two elements in a list

def swap(list):
    
    size=len(list)
    
    temp = list[1]
    list[1]=list[size-2]
    list[size-2]=temp
    
    return list

list=[10,54,85,22]
print(swap(list))