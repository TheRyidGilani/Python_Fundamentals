class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print("User Information:")
        print("First Name:", self.first_name.title())
        print("Last Name:", self.last_name.title())
        print("Age:", str(self.age))
        print("Email:", self.email)
        print("Location:", self.location.title())

    def greet_user(self):
        print("Hello, " + self.first_name.title() + "! Welcome back.")

class Admin(User):

    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = []

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print("- " + privilege)

# Create an instance of Admin
admin_user = Admin("John", "Doe", 30, "john.doe@example.com", "AdminLand")

# Add privileges to the admin user
admin_user.privileges = ["can add post", "can delete post", "can ban user"]

# Call the show_privileges method
admin_user.show_privileges()
