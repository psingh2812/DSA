## Program to search an element from a list of element using binary search algorithm

# myList -> it should be sorted in ascending order

def binarySearch(myList:[],target:int):
    low = 0
    high = len(myList)-1
    while low <= high:
        mid = (low+high)//2
        if myList[mid] > target:
            high = mid-1
        elif myList[mid] < target:
            low = mid+1
        else:
            return mid
    return -1

a = [1,2,4,6,23,34,45]
s = 1

result = binarySearch(a,s)

if result == -1:
    print("Not found!!")
else:
    print("Element found at index: ",result)
    