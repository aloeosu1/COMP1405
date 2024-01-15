amount = input("What is the bill amount? ")
percent = input("What percent do you want to tip? ")

amount = float(amount)
percent = int(percent)
tip = amount * (percent/100)

print(f"Your tip is ${tip:.2f}")

total = tip + amount

print(f"Your total is ${total:.2f}")



