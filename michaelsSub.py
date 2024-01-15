#Michael Han, 101157504, Assignment 2

#displaying welcome message
print("------------------------------------\n| Welcome to Michael's Sub Shoppe! |\n------------------------------------")

#loops until user picks valid sub option
while True:

    #printing sub options
    subSelect = input("Please select a sub (1-4): \n1. \"Meat\"-ball sub ($7.99)\n2. Cold Cut Club sub ($8.25)\
    \n3. Philly's Cheese Mis-Steak sub ($9.55)\n4. Veggie Pile sub ($6.75)\n\nSub: ")
    #if user enters 1
    if (subSelect == "1"):
        print(f"You picked sub {subSelect}, \"Meat\"-ball sub")
        #setting sub name
        sub = "\"Meat\"-ball sub"
        subCost = 7.99
        break
    #if user enters 2
    elif (subSelect == "2"):
        print(f"You picked sub {subSelect}, Cold Cut Club sub")
        #setting sub name
        sub = "Cold Cut Club sub"
        subCost = 8.25
        break
    #if user enters 3
    elif (subSelect == "3"):
        print(f"You picked sub {subSelect}, Philly's Cheese Mis-Steak sub")
        #setting sub name
        sub = "Philly's Cheese Mis-Steak sub"
        subCost = 9.55
        break
    #if user enters 4
    elif (subSelect == "4"):
        print(f"You picked sub {subSelect}, Veggie Pile Sub")
        #setting sub name
        sub = "Veggie Pile sub"
        subCost = 6.75
        break
    #if user enters blank input
    elif (subSelect == ""):
        print("Please pick a sub\n")
    #if user enters invalid option
    else:
        print(f"Sorry, {subSelect} is not an option\n")


#setting inital total toppings to nothing
totalToppings = ""

#printing topping options
print("Select any of the following toppings and hit enter:\nlettuce, tomatoes, onions, peppers,\
 jalepenos, pickles, cucumbers, olives, and/or guacamole. Guacamole is an extra $1.50")

#telling user to type done when they're done choosing toppings
print("Type \"done\" when you're done choosing toppings")

#loops until user enters "done"
while True:
    #getting user to enter topping
    topping = str(input("> "))
    
    #if user picks lettuce
    if (topping == "lettuce"):
        #adding lettuce to total toppings list
        totalToppings += "lettuce "
    
    #if user picks tomatoes
    elif(topping == "tomatoes"):
        #adding tomatoes to total toppings list
        totalToppings += "tomatoes "
    
    #if user picks onions
    elif(topping == "onions"):
        #adding onions to total toppings list
        totalToppings += "onions "
    
    #if user picks peppers
    elif(topping == "peppers"):
        #adding peppers to total toppings list
        totalToppings += "peppers "

    #if user picks jalepenos
    elif(topping == "jalepenos"):
        #adding jalepenos to total toppings list
        totalToppings += "jalepenos "

    #if user picks pickles
    elif(topping == "pickles"):
        #adding pickles to total toppings list
        totalToppings += "pickles "

    #if user picks cucumbers
    elif(topping == "cucumbers"):
        #adding cucumber to total toppings list
        totalToppings += "cucumbers "
    
    #if user picks olives
    elif(topping == "olives"):
        #adding olives to total toppings list
        totalToppings += "olives "

    #if user picks guacamole (extra $1.50)
    elif(topping == "guacamole"):
        totalToppings += "guacamole "
        #adding $1.50 to total cost
        subCost += 1.5

    #if user enters "done"    
    elif (topping == "done"):
        break
    
    #if user enters invalid option
    else:
        print(f"{topping} is not an option. Please pick from the list")

#printing order for confirmation
print(f"Your order: \nSub: {sub}\nToppings: {totalToppings}")


#loop asks user for "y" or "n" until they enter one or the other
while True:
    #asking user for "y" or "n"
    confirm = input("Is this what you want? (y/n)\n>")
    
    #if user enters y
    if (confirm == "y"):
        #calculating tax and final cost
        tax = subCost * 0.13
        totalCost = subCost + tax
        #printing receipt
        print("\n\n     Michael's Sub Shoppe")
        print("\n-------------------------------")
        print(f"Subtotal:\t\t${subCost:.2f}")
        print(f"Tax:\t\t\t${tax:.2f}")
        print("-------------------------------")
        print(f"Total:\t\t\t${totalCost:.2f}")
        print("-------------------------------")
        break
    
    #if user enters n
    elif (confirm == "n"):
        print("Sorry, please try ordering again. ")
        break
    
    #if user enters anything else (loops back, asks user for input again)
    else:
        print("Please enter \"y\" or \"n\"")