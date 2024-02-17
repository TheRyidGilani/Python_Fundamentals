from random import randint

class Die:
    def __init__(self, sides=10):
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and the number of sides."""
        result = randint(1, self.sides)
        print(f"The die with {self.sides} sides rolled: {result}")

# Create a 6-sided die and roll it 10 times
six_sided_die = Die()
for _ in range(10):
    six_sided_die.roll_die()

# Create a 10-sided die and roll it 10 times
ten_sided_die = Die(sides=10)
for _ in range(10):
    ten_sided_die.roll_die()

# Create a 20-sided die and roll it 10 times
twenty_sided_die = Die(sides=20)
for _ in range(10):
    twenty_sided_die.roll_die()
