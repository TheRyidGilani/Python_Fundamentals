while True:
    age = int(input("How old are you? "))

    if 0 < age < 3:
        print("The ticket is free.")
        break
    elif 3 <= age < 12:
        print("The ticket is $10.")
        break
    elif age >= 12:
        print("The ticket is $15.")
        break
    else:
        print("Please enter a valid age.")
        continue  # This will continue the loop and ask for the age again
