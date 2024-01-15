#importing random
import random

def makeRandomList(n):
    #making empty list
    lis = []
    #looping for n times
    for i in range (n):
        #inserting random integer between 1 and 100 into list
        lis.insert(i, random.randint(1,100))
    #returns list
    return lis

def main():
    n = int(input("Please enter the list length: "))
    lis = makeRandomList(n)
    print(lis)

main()
