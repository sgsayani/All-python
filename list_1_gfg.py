list1 = ["sayani","sonali","kakali","sanjoy"]

print(list1)



#Python program to interchange first and last elements in a list

def swap(list):
    size=len(list)
    temp = list[0]
    list[0]=list[size-1]
    list[size-1]=temp
    
    return(list)
list=[1,2,45,74]
print(swap(list))