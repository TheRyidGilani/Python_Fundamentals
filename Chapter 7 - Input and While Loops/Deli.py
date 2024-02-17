sandwich_orders = ['Meat', 'Pastrami', 'Vegetarian', 'Pastrami', 'Cheese', 'Pastrami', 'Tuna']
finished_sandwiches = []

print("The Deli has run out of Pastrami")


while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)


for name in finished_sandwiches:
    print("I made your " + name + " sandwich")
