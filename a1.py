#This searching algorithm will sequentially check the elements and if the element is found , we shall return
#the index else -1 

def linearSearch(arr,k):
    for i in range(0, len(arr)):
        if arr[i]==k:
            return i
    return -1

arr = [10,23,45,70,11,15]
k = 11
result = linearSearch(arr,k)
if result!=-1:
    print(f"Element is found at index : {result}")
else:
    print("Sorry Wrong Input")