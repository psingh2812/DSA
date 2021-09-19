# Write a program to sort list of elements using quick sort algorithm
def partition(a:[], start:int, end:int):

    pivot = a[start]
    pivot_idx = start
    left = start+1
    right = end

    while left <= right:

        while left <= end and a[left] < pivot:
            left = left+1

        while a[right] > pivot and right > start:
            right = right-1

        if left < right:
            a[left], a[right] = a[right], a[left]

    a[pivot_idx],a[right] = a[right], a[pivot_idx]
    return right

def quickSort(a:[], start:int, end:int):

    if start < end :
        idx = partition(a, start, end)
        quickSort(a, start, idx-1)
        quickSort(a, idx+1, end)
    return

#a = [1,70,60,50,30,100,10]
quickSort(a, 0, len(a)-1)
print(a)