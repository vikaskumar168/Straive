# Define a Class
class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    # Method
    def drive(self):
        print(f"{self.brand} {self.model} is driving...")


# Create Objects
car1 = Car("Tesla", "Model S")
car2 = Car("Toyota", "Corolla")

# Access Attributes
print(car1.brand)  # Tesla
print(car2.model)  # Corolla

# Call Method
car1.drive()  # Tesla Model S is driving...
