class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print("The name of the restaurant is: " + self.name.title())
        print("Its cuisine is: " + self.cuisine.title())

    def open_restaurant(self):
        print("The restaurant is open")

# Create an instance of the Restaurant class
restaurant = Restaurant("Great Eats", "Italian")

# Print the attributes individually
print("Restaurant Name:", restaurant.name.title())
print("Cuisine Type:", restaurant.cuisine.title())
print("\n")

# Call the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
