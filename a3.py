def merge_sort_alg(arr,left,mid,right):
    i = left
    j = mid+1
    k = 0
    
    temp = [0]*(right-left+1)
    while(i<=mid and j<=right):
        if(arr[i]<arr[j]):
            temp[k]=arr[i]
            i += 1
            k += 1
        else:
            temp[k]=arr[j]
            j +=1
            k +=1
            
    while(i<=mid):
        temp[k]=arr[i]
        i += 1
        k += 1
        
    while(j<=right):
        temp[k]=arr[j]
        j += 1
        k += 1
        
    for i in range(len(temp)):
        arr[left+i]=temp[i]
        
    
    
def merge_sort(arr,left,right):
    if(left>=right):
        return
    mid = (left+right)//2
    merge_sort(arr,left,mid)
    merge_sort(arr,mid+1,right)
    merge_sort_alg(arr,left,mid,right)
    
arr = [12,45,11,67,33,68]
merge_sort(arr ,0 , len(arr)-1)
print(arr)