class Dog:
    """This is a dog"""

    def __init__(self, name, age):
        """Initialize name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """Make the dog sit"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} has rolled over")

### Adding a dog ###

my_dog = Dog('Simba', 9)

print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()


#### Restaurant Excercise ####
class Restaurant:
    """A simple model of a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"{self.name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Indicate that the restaurant is open"""
        print(f"{self.name} is now open!")
        
# Creating an instance of Restaurant
my_restaurant = Restaurant('Baratie', 'Seafood')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# Creating another instance of Restaurant
chop_lick_fingers = Restaurant('Chop Lick Fingers', 'Barbecue')
chop_lick_fingers.describe_restaurant()

# Creating another instance of Restaurant
pasta_palace = Restaurant('Pasta Palace', 'Italian')
pasta_palace.describe_restaurant()

## Creating a User Class ##
class User:
    """A simple model of a user profile"""

    def __init__(self, first_name, last_name, age):
        """Initialize user profile"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """Describe the user"""
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}")

    def greet_user(self):
        """Greet the user"""
        print(f"Hello, {self.first_name} {self.last_name}!")
        
# Creating an instance of User
user1 = User('John', 'Doe', 30)
user1.describe_user()
user1.greet_user()

# Creating another instance of User
user2 = User('Jane', 'Smith', 25)
user2.describe_user()  
user2.greet_user()

# Creating another instance of User
user3 = User('Alice', 'Johnson', 28)
user3.describe_user()
user3.greet_user()