#Michael Han, 101157504, Tutorial 5, problem 3
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
        

            