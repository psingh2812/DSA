# Write a program to sort list of elements using selection sort algorithm

def selectionSort(myList:[]):
    
    for i in range(len(myList),1,-1):
        indexLargest = 0
        for j in range(1,i):
            if myList[j] > myList[indexLargest]:
                indexLargest = j        
        myList[indexLargest],myList[i-1] = myList[i-1],myList[indexLargest]               
        #print("i,j",i,j)
        #print(myList)
    return myList

a = [1,70,60,50,30,20,10]

print(selectionSort(a))