class Restaurant:
    def __init__(self, name):
        self.name = name
        self.number_served = 0

    def display_number_served(self):
        served = self.name + " has served " + str(self.number_served) + " customers today."
        return served

    def increment_number_served(self, customer):
        self.number_served += customer


# Display the number of customers
my_restaurant = Restaurant("Gilani's")
print(my_restaurant.display_number_served())

# 23 new customers just walked in!
my_restaurant.increment_number_served(23)

# Display the updated number of customers
print(my_restaurant.display_number_served())
