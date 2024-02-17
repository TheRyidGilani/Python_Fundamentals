pizza = []
topping = input("Enter a topping for your pizza (type 'quit' to finish): ")

while topping.lower() != 'quit':
    pizza.append(topping)
    topping = input("Enter another topping (type 'quit' to finish): ")

print("Your pizza will have the following toppings:")
for item in pizza:
    print(item)
