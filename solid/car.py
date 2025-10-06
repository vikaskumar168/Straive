class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def drive(self):
        print(f"{self.brand} {self.model} is driving...")

    def findPrice(self):
        print(f"Price of {self.brand} {self.model} is ${self.price}")


car1 = Car("Tesla", "Model S", 25000)
car2 = Car("Toyota", "Corolla", 33333)

print(car1.brand)
print(car2.model)

car1.drive()
car2.findPrice()