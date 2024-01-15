#tutorial 3, problem 1
import random
#getting random operator
op = random.randint(1, 3)
#if operator is plus (1)
if (op == 1):
    #getting two random integers from 1 to 100
    intOne = random.randint(1, 100)
    intTwo = random.randint(1, 100)
    #adding two integers
    ans = intOne + intTwo
    #asking user for answer
    uAns = int(input(f"{intOne} + {intTwo} = "))
    #checking user's answer
    if (uAns == ans):
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {ans}")

#if operator is minus (2)
if (op == 2):
    intOne = random.randint(1, 100)
    intTwo = random.randint(1, 100)
    ans = intOne - intTwo
    uAns = int(input(f"{intOne} - {intTwo} = "))
    if (uAns == ans):
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {ans}")

#if operator is times (3)
if (op == 3):
    intOne = random.randint(1, 100)
    intTwo = random.randint(1, 100)
    ans = intOne * intTwo
    uAns = int(input(f"{intOne} * {intTwo} = "))
    if (uAns == ans):
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {ans}")



