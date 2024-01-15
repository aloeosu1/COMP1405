#Michael Han, 101157504, Tutorial 5, problem 2

#this function converts a decimal number to a binary number
def decToBin(x):
    #setting binary string to blank
    binNum=""
    #finding largest power of 2 less than or equal to decimal number using pow2 function
    p = pow2(x)
    print(p)
    #loop while p is greater than or equal to 1
    while (p>=1):
        #if p is less than or equal to x
        if p<=x:
            x -=p
            binNum+="1"
        else:
            binNum+="0"
        #divide p by 2
        p = p / 2
    
    print(binNum)
#finding largest power of 2 less than or equal to decimal number (function from problem 1)
def pow2(num):
    i = 0
    x=0
    while (x<=num):
        
        x = 2**i
        i+=1  
    x = 2**(i-2)
    #returns largest power of 2 less than or equal to decimal number to decToBin function
    return x


