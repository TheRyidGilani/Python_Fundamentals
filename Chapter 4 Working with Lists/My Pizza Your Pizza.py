my_pizza = ['cheese', 'veggie','meat lovers']
friends_pizza = my_pizza[:]

my_extra_pizza = 'Halal Pepperoni'
my_pizza.append(my_extra_pizza)

friends_extra_pizza = 'Haram Pepperoni'
friends_pizza.append(friends_extra_pizza)

print("My favourite types of pizza include: " )

for mypizza in my_pizza:
    print(mypizza)

print("\nMy friends favourite types of pizza include: " )

for myfriendspizza in friends_pizza:
    print(myfriendspizza)
