magicians = ['Ryid', 'Jim', 'Atreus', 'Nihal']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    return ["The Great " + name for name in magicians]


print("Original list of magicians:")
show_magicians(magicians)

great_magicians = make_great(magicians)
print("\nList of magicians after modification:")
show_magicians(great_magicians)
