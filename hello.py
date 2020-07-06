toppings = []
while True:
    topping = input("What should be on your Pizza? ")
    if topping == 'q':
        break
    else:
        toppings.append(topping)


print(toppings)
print("Leckere Pizza")