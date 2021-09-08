## Program to search a element from a list of elements

def linearSearch(mylist:[],target:int):
    for i in range(len(mylist)):
        if mylist[i] == target:
            return i
    return -1


a = [1,32,43,54,100,203]
s = 31
result = linearSearch(a,s)
if result == -1:
    print("Not found!!")
else:
    print("Element found at position :", result)