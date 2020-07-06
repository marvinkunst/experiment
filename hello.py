toppings = []
print("Geben Sie ihre Toppings für die Pizza ein! ")
print('press q to end')

while True:
    topping = input("What should be on your Pizza? ")
    if topping == 'q':
        break
    else:
        toppings.append(topping)

print("Ihre Pizza hat folgende Toppings:")
for topping in toppings:
    print(f'-{topping.title()}')
