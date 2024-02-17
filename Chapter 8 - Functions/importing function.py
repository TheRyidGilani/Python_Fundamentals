# Approach 1: Import the entire module
import sandwich_maker

# Call the function from the imported module
sandwich_maker.make_sandwich("Ham", "Cheese", "Lettuce")

# Approach 2: Import the function directly
from sandwich_maker import make_sandwich

# Call the function directly
make_sandwich("Turkey", "Swiss")

# Approach 3: Import with an alias
import sandwich_maker as sm

# Call the function using the alias
sm.make_sandwich("Peanut Butter", "Jelly", "Banana", "Honey")
