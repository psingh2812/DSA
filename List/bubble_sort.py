# Write a program to sort list of elements using bubble sort algorithm

def bubbleSort(myList:[]):

    for i in range(len(myList),1,-1):
        for j in range(i-1):
            if myList[j] > myList[j+1]:
                myList[j],myList[j+1] = myList[j+1],myList[j]
        #print("i,j",i,j)
        #print(myList)
    return myList

a = [90,80,60,40,30,20]

print(bubbleSort(a))