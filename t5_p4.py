#Michael Han, 101157504, Tutorial 5, problem 4
#this program combines the some of the other functions in the tutorial and a new main function and creates a minigame
import random

#this function converts a decimal number to a binary number
def decToBin(x):
    #setting binary string to blank
    binNum=""
    #finding largest power of 2 less than or equal to decimal number using pow2 function
    p = pow2(x)
    
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
    
    return binNum
    
    
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

#this function takes an integer as an arguement, asks user for corresponding binary number
def userBin(n):
    print(f"Your number is {n}.")
    userAns=""
    #loops and reprompts user if they have blank input
    while (userAns == ""):
        #getting user input
        userAns = str(input("Enter the corresponding binary number: "))
        #if user inputs something
        if (userAns != ""):
            #return their input
            return userAns
#main function
def main():
    print("Welcome to Michael's Binary Quiz Game!\tPlease type \"stop\" to exit")
    points = 0
    while True:
        num = random.randint(0, 256)
        #calling user input function
        userAns = userBin(num)
        #calling decToBin function to calculate correct answer
        ans = decToBin(num)
        if userAns=="stop":
            break
        else:
            #if user's answer matches correct answer
            if userAns==ans:
                print("Correct!")
                points += 1
                print(f"Score: {points}")
                #if user's answer doesn't match correct answer
            elif (userAns!=ans):
                print(f"Incorrect! The correct answer is {ans}")
                print(f"Score: {points}")
    
    print("Thanks for playing")
    print(f"Final score: {points}")
        

main()


