def make_shirt(size):
    if size.lower() == 'large':
        text = 'I love python'
    elif size.lower() == 'medium':
        text = 'I hate python'
    else:
        text = 'I love Java'
    print("The size of your shirt is: " + size.title())
    print("The text on your shirt is: " + text.title())

shirt = input("Select A Shirt Size:" )

make_shirt(shirt)