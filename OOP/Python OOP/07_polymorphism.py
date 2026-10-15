# ==========================================
# PYTHON OOP - POLYMORPHISM
# ==========================================


# 1. Parent Class

class Vehicle:
    def move(self):
        print("Vehicle is moving")


# 2. Child Classes with Method Overriding

class Car(Vehicle):
    def move(self):
        print("Car is driving")


class Bus(Vehicle):
    def move(self):
        print("Bus is carrying passengers")


class Truck(Vehicle):
    def move(self):
        print("Truck is carrying goods")


# 3. Creating Objects

car = Car()
bus = Bus()
truck = Truck()


# 4. Same Method, Different Behavior

car.move()
bus.move()
truck.move()

print("--------------------")


# 5. Polymorphism with a List and Loop

vehicles = [car, bus, truck]

for vehicle in vehicles:
    vehicle.move()

print("--------------------")


# 6. Polymorphism with a Function

def start_moving(vehicle):
    vehicle.move()


start_moving(car)
start_moving(bus)
start_moving(truck)

print("--------------------")


# 7. Polymorphism without Inheritance

class Dog:
    def sound(self):
        print("Dog says: Bark")


class Cat:
    def sound(self):
        print("Cat says: Meow")


dog = Dog()
cat = Cat()

animals = [dog, cat]

for animal in animals:
    animal.sound()

print("--------------------")


# 8. Practical Payment Example

class CardPayment:
    def pay(self, amount):
        print("Paid", amount, "using Card")


class CashPayment:
    def pay(self, amount):
        print("Paid", amount, "using Cash")


class MobilePayment:
    def pay(self, amount):
        print("Paid", amount, "using Mobile Banking")


payments = [CardPayment(), CashPayment(), MobilePayment()]

for payment in payments:
    payment.pay(1000)