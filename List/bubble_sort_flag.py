# Write a program to sort list of elements using bubble sort algorithm adding a IsSortedFlag

def bubbleSort(myList:[]):
    
    for i in range(len(myList),1,-1):
        isSortedFlag = -1
        for j in range(i-1):
            if myList[j] > myList[j+1]:
                myList[j],myList[j+1] = myList[j+1],myList[j]
                isSortedFlag = 1
        if isSortedFlag == -1:
            print("No need to traverse further")
            return myList               
        #print("i,j",i,j)
        #print(myList)
    return myList

a = [20,30,15,35,45,50,65]

print(bubbleSort(a))