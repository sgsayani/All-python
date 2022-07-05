def triplets(arr,n,sum):
    for i in range (0,n-2):
     for j in range(i+1,n-1):
         for k in range (j+1,n):
             if (arr[i]+arr[j]+arr[k]==sum):
                 print(arr[i], arr[j], arr[k],s="")
arr=[0,1,2,-3,7,8,74,-9,10,-52]
n=len(arr)
sum=-2
triplets(arr, n, sum)     