# ==========================================
# PYTHON OOP - ABSTRACT CLASS AND METHOD
# ==========================================


# 1. Import ABC and abstractmethod

from abc import ABC, abstractmethod


# 2. Abstract Parent Class

class Vehicle(ABC):

    def __init__(self, name):
        self.name = name

    # Normal method
    def show_name(self):
        print("Vehicle Name:", self.name)

    # Abstract method
    @abstractmethod
    def move(self):
        pass


# 3. Car Child Class

class Car(Vehicle):

    def move(self):
        print(self.name, "is driving on the road")


# 4. Bus Child Class

class Bus(Vehicle):

    def move(self):
        print(self.name, "is carrying passengers")


# 5. Truck Child Class

class Truck(Vehicle):

    def move(self):
        print(self.name, "is carrying goods")


# 6. Creating Child Objects

car1 = Car("Toyota Corolla")
bus1 = Bus("Volvo Bus")
truck1 = Truck("Tata Truck")


# 7. Using Normal Parent Method

car1.show_name()
bus1.show_name()
truck1.show_name()

print("--------------------")


# 8. Using Implemented Abstract Methods

car1.move()
bus1.move()
truck1.move()

print("--------------------")


# 9. Another Abstract Class Example

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Card")


class CashPayment(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Cash")


# 10. Creating Payment Objects

card = CardPayment()
cash = CashPayment()

card.pay(1000)
cash.pay(500)


# This would cause an error:
# vehicle = Vehicle()
# payment = Payment()