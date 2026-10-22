# ==========================================
# PYTHON OOP - INHERITANCE BASICS
# ==========================================


# 1. Parent Class

class Vehicle:

    def __init__(self, name, vehicle_number):
        self.name = name
        self.vehicle_number = vehicle_number

    def start(self):
        print(self.name, "started")

    def show_basic_info(self):
        print("Name:", self.name)
        print("Vehicle Number:", self.vehicle_number)


# 2. Car Child Class

class Car(Vehicle):

    def __init__(self, name, vehicle_number, number_of_doors):
        super().__init__(name, vehicle_number)
        self.number_of_doors = number_of_doors

    def show_car_info(self):
        self.show_basic_info()
        print("Number of Doors:", self.number_of_doors)


# 3. Bus Child Class

class Bus(Vehicle):

    def __init__(self, name, vehicle_number, passenger_capacity):
        super().__init__(name, vehicle_number)
        self.passenger_capacity = passenger_capacity

    def show_bus_info(self):
        self.show_basic_info()
        print("Passenger Capacity:", self.passenger_capacity)


# 4. Truck Child Class

class Truck(Vehicle):

    def __init__(self, name, vehicle_number, load_capacity):
        super().__init__(name, vehicle_number)
        self.load_capacity = load_capacity

    def show_truck_info(self):
        self.show_basic_info()
        print("Load Capacity:", self.load_capacity, "tons")


# 5. Creating Car Object

car1 = Car(
    "Toyota Corolla",
    "DHAKA-1234",
    4
)

print("Car Information")
car1.show_car_info()
car1.start()

print("--------------------")


# 6. Creating Bus Object

bus1 = Bus(
    "Volvo Bus",
    "DHAKA-5678",
    50
)

print("Bus Information")
bus1.show_bus_info()
bus1.start()

print("--------------------")


# 7. Creating Truck Object

truck1 = Truck("Tata Truck", "DHAKA-9012", 10)

print("Truck Information")
truck1.show_truck_info()
truck1.start()