# ==========================================
# PYTHON OOP - MULTI-LEVEL INHERITANCE
# ==========================================


# 1. Parent Class

class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

    def start(self):
        print(self.brand, "vehicle started")


# 2. Child Class

class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        print("Model:", self.model)

    def drive(self):
        print(self.brand, self.model, "is driving")


# 3. Child of Car

class ElectricCar(Car):

    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def show_battery(self):
        print("Battery:", self.battery, "kWh")

    def charge(self):
        print(self.brand, self.model, "is charging")


# 4. Creating an ElectricCar Object

car1 = ElectricCar("Tesla", "Model 3", 75)


# 5. Using Method from Vehicle

car1.show_brand()
car1.start()

print("--------------------")


# 6. Using Method from Car

car1.show_model()
car1.drive()

print("--------------------")


# 7. Using ElectricCar's Own Method

car1.show_battery()
car1.charge()

print("--------------------")


# 8. Showing All Information

print("Electric Car Information")
print("Brand:", car1.brand)
print("Model:", car1.model)
print("Battery:", car1.battery, "kWh")