# vehicle
class Vehicle:
    def show(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Car Brand:", self.brand)

class Bike(Vehicle):
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Bike Brand:", self.brand)

car = Car(input("Enter car brand: "))
bike = Bike(input("Enter bike brand: "))

car.show()
bike.show()


#Animal
class Animal:
    def sound(self):
        print("Animals make sounds.")

class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()