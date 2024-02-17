Available_names = ['Admin','Ryid','Sam','Azzy','Nihal']

if Available_names:
    for names in Available_names:
        if names == 'Admin':
            print("Welcome Admin, would you like to see a progress report?")
        else:
          print("Hello " + names + ", thank you for logging in")

else:
    print("We need to find some more users")