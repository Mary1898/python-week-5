#desgning a class
# Defining the Smartphone class
class Smartphone:
    def __init__(self, brand, model, price):
        """
        Constructor to initialize the smartphone attributes.
        """
        self.brand = brand
        self.model = model
        self.price = price
    
    def call(self, number):
        """
        Simulates making a call.
        """
        print(f"{self.brand} {self.model} is calling {number}...")
    
    def display_info(self):
        """
        Displays the smartphone's details.
        """
        print(f"Smartphone: {self.brand} {self.model}, Price: ${self.price}")

# Creating a subclass for a specific type of Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        """
        Extends the Smartphone class with a GPU attribute.
        """
        super().__init__(brand, model, price)
        self.gpu = gpu
    
    def play_game(self, game):
        """
        Simulates playing a game.
        """
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU.")

# Example usage
phone = Smartphone("Samsung", "Galaxy S23", 799)
phone.display_info()
phone.call("123-456-7890")

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 999, "Adreno 730")
gaming_phone.display_info()
gaming_phone.play_game("PUBG Mobile")


#Polymorphism Challenge

# Base class: Vehicle
class Vehicle:
    def move(self):
        """
        Base method to describe movement.
        """
        print("The vehicle moves in its own way.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        """
        Overrides the move method to specify driving.
        """
        print("The car is driving .")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        """
        Overrides the move method to specify flying.
        """
        print("The plane is flying .")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        """
        Overrides the move method to specify sailing.
        """
        print("The boat is sailing .")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

