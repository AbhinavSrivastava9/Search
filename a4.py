def quickAlg(arr,low,high):
    i = low
    j = high
    pivot = arr[low]
    while(i<j):
        while(arr[i]<=pivot and i<=high):
            i += 1
        while(arr[j]>pivot and j>=low):
            j -= 1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j
    

def quick_sort(arr,low,high):
    if low<high:
        pivot_index = quickAlg(arr,low,high)
        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1, high)
        
arr = [12,45,11,9,42,8,66]
quick_sort(arr,0,len(arr)-1)
print(arr)