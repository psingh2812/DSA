## Program to search an element from a list of element using binary search recurrsive algorithm
# myList -> it should be sorted in ascending order

def binarySearch(myList:[], target:int, low:int, high:int):
    
    if low > high:
        return -1

    mid = (low+high)//2
    if myList[mid] > target:
        return(binarySearch(myList, target, low, mid-1))
    elif myList[mid] < target:
        return(binarySearch(myList, target, mid+1, high))
    else:
        return mid


a = [1,2,4,6,23,34,45,56]
s = 45

result = binarySearch(a,s,0,len(a)-1)

if result == -1:
    print("Not found!!")
else:
    print("Element found at index: ",result)
    