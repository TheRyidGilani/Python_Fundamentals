class Car():

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        odometer_reading = "This car has " + str(self.odometer_reading) + " miles on it."
        return odometer_reading

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            return "You can't roll back an odometer!"

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
            return "Added " + str(miles) + " miles to the odometer."
        else:
            return "You can't add negative miles to the odometer!"

# Create a new Car instance
my_new_car = Car('Honda', 'Civic', '2020')

# Get and print the descriptive name of the car
print(my_new_car.get_descriptive_name())

# Set the odometer reading to 23 and read the odometer
my_new_car.odometer_reading = 23
print(my_new_car.read_odometer())

# Update the odometer reading to 23500
my_new_car.update_odometer(23500)
print(my_new_car.read_odometer())

# Increment the odometer by 100 miles and read the odometer
add_miles = my_new_car.increment_odometer(100)
print("\n"+add_miles)
print(my_new_car.read_odometer())