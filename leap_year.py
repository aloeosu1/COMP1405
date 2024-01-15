#tutorial 3, problem 2
#asking user for a year
year = int(input("Enter a year: "))
#if the year is divisible by 4 (every 4 years)
if(year % 4 == 0):
    #checking if it's every 100 years
    if (year % 100 == 0):
        #checking if it's every 400 years
        if (year % 400 == 0):
            print(f"The year {year} is a leap year!")
        #if it's not every 400th year
        else:
             print(f"The year {year} is not a leap year!")
    #if not divisble by 100, but divisible by 4
    else:
        print(f"The year {year} is a leap year!")


    
#if not divisble by 4
else:
    print(f"The year {year} is not a leap year!")