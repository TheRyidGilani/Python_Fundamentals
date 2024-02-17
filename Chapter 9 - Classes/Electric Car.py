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

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self,battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        return "This car has a " + str(self.battery_size) + "-kWh battery."

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
class ElectricCar(Car):
    """"Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class. Then initialize attributes specific to electric vehicles."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('Tesla', 'Cybertruck', '2024')
print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery())
my_tesla.battery.get_range()