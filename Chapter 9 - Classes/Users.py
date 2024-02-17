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

# Create several instances of the User class
user1 = User("John", "Doe", 25, "john.doe@example.com", "New York")
user2 = User("Alice", "Smith", 30, "alice.smith@example.com", "London")
user3 = User("Bob", "Johnson", 22, "bob.johnson@example.com", "Paris")

# Call both methods for each user
user1.describe_user()
user1.greet_user()

print("\n")

user2.describe_user()
user2.greet_user()

print("\n")

user3.describe_user()
user3.greet_user()
