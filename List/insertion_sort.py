# Write a program to sort list of elements using insertion sort algorithm

def insertionSort(myList:[]):
    
    for i in range(1,len(myList)):
        key = myList[i]
        j = i-1
        while(j>=0 and key < myList[j]):
            myList[j+1] = myList[j]
            j = j-1
        myList[j+1] = key
        #print("i,j",i,j)
        #print(myList)
    return myList

a = [1,70,60,50,30,100,10]
print(insertionSort(a))