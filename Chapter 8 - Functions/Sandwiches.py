def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item)
    print("Sandwich is ready!\n")

# Call the function with different numbers of arguments
make_sandwich("Ham", "Cheese", "Lettuce")
make_sandwich("Turkey", "Swiss")
make_sandwich("Peanut Butter", "Jelly", "Banana", "Honey")
