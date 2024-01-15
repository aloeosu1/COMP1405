#Michael Han, Tutorial 8
import random

#this function takes an integer and generates n sublists with n elements random grid
def generateRandomGrid(n):
    #starting with empty grid
    grid = []
    #generates n sublists
    for i in range(0, n):
        grid.append([])
        #filling in sublists with n random numbers from 1 - 100
        for j in range(0,n):
            #getting random number
            rand = random.randint(0,100)
            #adding number to sublist
            grid[i].append(rand)
    
    return grid

#this function searches grid for the smallest element
def searchGrid(grid):
    #assume first index of first sublist is smallest
    smallestSoFar = grid[0][0]
    #looping through every sublist
    for i in range(0, len(grid)):
        #looping through every index in each sublist
        for j in range(0, len(grid)):
            #if the element in the index in sublist is smaller than the smallest so far
            if grid[i][j]<smallestSoFar:
                #make that index the smallest so far
                smallestSoFar = grid[i][j]
    return smallestSoFar

def main():
    grid = generateRandomGrid(6)
    print(grid)
    smallest = searchGrid(grid)
    print(smallest)


main()