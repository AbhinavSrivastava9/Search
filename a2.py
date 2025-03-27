def BinarySearch(arr,k):
    i = 0 
    j = len(arr)-1
    
    while(i<=j):
        mid = (i+j)//2 
        if arr[mid]==k:
            return mid
        elif k > arr[mid]:
            i = mid+1 
        else:
            j = mid-1
    return -1

arr = [10,20,30,40,50,60]
k = 0
result = BinarySearch(arr,k)
if result!=-1:
    print(f"Element is found at index : {result}")
else:
    print("Sorry Wrong Input")