class Restaurant:
    def __init__(self, name, cuisine):
        """Initialize attributes to describe a restaurant."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Print information about the restaurant."""
        print(f"The name of the restaurant is: {self.name.title()}")
        print(f"Its cuisine is: {self.cuisine.title()}")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print("The restaurant is open")

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine):
        # Call parent class constructor
        super().__init__(name, cuisine)
        # Attach list of flavors as attribute
        self.flavors = []

    def display_flavors(self):
        print("\nAvailable Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Create an instance of the IceCreamStand class
ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream Parlor")
ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]

# Display restaurant information and ice cream flavors
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
ice_cream_stand.open_restaurant()
