#Michael Yisheng Han, Student Number 101157504
#Assignment 1, Problem 5
import math
#asking user for three side lengths of a triangle
print("Please enter 3 side lengths of a triangle")
a = int(input("Side A: "))
b = int(input("Side B: "))
c = int(input("Side C: "))
#calculating S
S = (a + b + c) / 2
#calculating area of triangle using Heron's formula
area = math.sqrt(S * (S - a) * (S - b) * (S - c))
#printing area 
print(f"A triangle with side lengths {a}, {b}, and {c} will have an area of {area:.4f}")