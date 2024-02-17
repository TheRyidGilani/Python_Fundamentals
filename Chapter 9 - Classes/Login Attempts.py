class User:
    MAX_LOGIN_ATTEMPTS = 3  # Adjust this threshold as needed

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        self.locked_out = False

    def describe_user(self):
        print("First Name:", self.first_name.title())
        print("Last Name:", self.last_name.title())

    def greet_user(self):
        print("Hello, " + self.first_name.title() + "! Welcome back.")

    def increment_login_attempts(self):
        if not self.locked_out:
            self.login_attempts += 1
            print("Login attempt #" + str(self.login_attempts))
            if self.login_attempts >= self.MAX_LOGIN_ATTEMPTS:
                print("Too many login attempts. Locked out.")
                self.locked_out = True

    def reset_login_attempts(self):
        self.login_attempts = 0
        self.locked_out = False
        print("Login attempts reset to 0.")

    def is_locked_out(self):
        return self.locked_out

# Create a new User instance
new_user = User('Ryid', 'gilani')

#Attempt to login 3 times
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

# Check if locked out
if new_user.is_locked_out():
    print("User is currently locked out.")
else:
    new_user.greet_user()
