#creating function
def removeDuplicates(L):
    #making blank list
    dupL = []
    #looping through each index in original list, adds it to dup list if it's not already in it
    for i in range (len(L)):
        if L[i] not in dupL:
            dupL.append(L[i])
    #returns value
    return dupL

def main():
    L = [1,5,3,1,2,7,1,3,5]
    final = removeDuplicates(L)
    print(final)

main()
