#Michael Han, 101157504, Tutorial 8 part 2

import random
import timeit

def linearSearchSmallest(lis):
    if len(lis)==0:
        return -1
    
    indexSmallestSoFar = 0
    for i in range(0, len(lis)):
        if lis[i]<lis[indexSmallestSoFar]:
            indexSmallestSoFar = i

    return lis[indexSmallestSoFar]

#must sort before using binary search
def binarySearchIfFound(lis, key):
    #set start = 0
    start = 0

    end = len(lis)-1

    while start <=end:
        #finding middle index value
        mid = (start+end)//2

        if lis[mid]==key:
            return mid

        elif lis[mid]>key:
            end = mid - 1

        else:
            start = mid + 1

    #if key not found in list
    return -1

def bubbleSort(lis):
    lis = lis[:]
    for i in range(0, len(lis)):
		#for each pair of items in the list
	    for j in range(1, len(lis)):
			#if pair is out of order
		    if lis[j-1] > lis[j]:
				#swap the two items
			    temp = lis[j-1] 
			    lis[j-1] = lis[j]
			    lis[j] = temp

    return lis


def randomList(n):
    lis = []
    for i in range (0, n):
        randNum = random.randint(0,100)
        lis.insert(i, randNum)

    return lis


def main():
    lis = randomList(1000)
    print(f"Random list is: {lis}")

    #timing
    before1 = timeit.default_timer()
    #finding smallest element in list
    smallest = linearSearchSmallest(lis)
    #after code runs
    after1 = timeit.default_timer()
    #finding time it took to run section of code
    lSearchTime = after1 - before1
    #printing smallest element
    print(f"Smallest element is: {smallest}")

    #timing
    before2 = timeit.default_timer()
    #sorting list
    sortedLis = bubbleSort(lis)
    #after code runs
    after2 = timeit.default_timer()
    #finding time
    sortTime = after2 - before2
    #printing sorted list
    print(f"From least to greatest: {sortedLis}")

    #timing
    before3 = timeit.default_timer()
    #binary search for a key
    indexOfKey = binarySearchIfFound(sortedLis, 2)
    #after code runs
    after3 = timeit.default_timer()
    #finding time
    bSearchTime = after3 - before3
    if indexOfKey == -1:
        print("Key not found")

    else:
        print(f"Key found at index: {indexOfKey}")

    print(lSearchTime)
    print(sortTime)
    print(bSearchTime)



main()