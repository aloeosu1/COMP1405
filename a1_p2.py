#Michael Yisheng Han, Student Number 101157504
#Assignment 1, Problem 2
#asks user for input in cm
cm = float(input("Enter a distance in centimeters (cm) "))
#calculating feet (using floor division)
feet = int(cm // 30.48)
#finding remaining centimeters (using modulus to find just the remainder)
rem = cm % 30.48
#finding inches (using remaining cm to convert to inches, rounding to nearest inch)
inches = round(rem / 2.54)
#preventing outputs like 5'12"
if (inches == 12):
    feet = feet + 1
    inches = 0

#printing distance in feet and inches
print(f"{cm} cm is approximately {feet}'{inches}\" ")