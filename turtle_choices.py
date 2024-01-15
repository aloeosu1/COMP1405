#tutorial 3, problem 4

import turtle
#printing drawing choices
print("1. Square\n2. Triangle\n3. Star")
#asking for user input
choice = int(input("Please choose an option 1, 2 or 3: "))
#asking for user input for color
color = input("Red/Green/Blue? ")

#choice 1 (square)
if (choice == 1):
    #setting color
    turtle.color(color)
    turtle.right(180)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)

#choice 2 (triangle)
if (choice == 2):
    turtle.color(color)
    turtle.right(60)
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(200)

#choice 3 (star)
elif (choice ==3):
    turtle.color(color)
    turtle.right(144)
    turtle.forward(200)
    turtle.right(144)
    turtle.forward(200)
    turtle.right(144)
    turtle.forward(200)
    turtle.right(144)
    turtle.forward(200)
    turtle.right(144)
    turtle.forward(200)



#ending program on click
turtle.exitonclick()