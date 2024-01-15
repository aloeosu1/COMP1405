#tutorial 3, problem 3
#asking user for a number representing months
month = int(input("Enter a number (month) from [1-12] "))
day = int(input("Enter a number (day) from [1-31] "))
 
#between March 20th and June 20th
if((month >=3 and day >= 20) or (month <= 6 and day <= 20)):
    print("The season is spring")
#between June 21st and September 22nd
elif((month >=6 and day >= 21) or (month <= 9 and day <= 22)):
    print("The season is summer")
#between September 23rd and December 20th
elif((month >=9 and day >= 23) or (month <=12 and day <= 20)):
    print("The season is fall")
#between December 21st and March 19th (anything else)
else:
    print("The season is winter")


