#Michael Yisheng Han, Student Number 101157504
#Assignment 1, Problem 4
#ask user to input 4 numbers
print("Please enter four numbers")
#number 1
a = int(input("Number 1: "))
#number 2
b = int(input("Number 2: "))
#number 3
c = int(input("Number 3: "))
#number 4
d = int(input("Number 4: "))
#finding the greatest number
great = max(a, b, c, d)
#finding the smallest number
least = min(a, b, c, d)
#finding the difference
diff = great - least
#displaying the largest difference
print(f"The largest difference is {diff}")