# ==========================================
# PYTHON OOP - FLEET MANAGEMENT INTRODUCTION
# ==========================================


# 1. Vehicle Class

class Vehicle:

    def __init__(self, name, vehicle_number, vehicle_type):
        self.name = name
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.available = True

    # Show vehicle information
    def show_info(self):
        print("Vehicle Name:", self.name)
        print("Vehicle Number:", self.vehicle_number)
        print("Vehicle Type:", self.vehicle_type)
        print("Status:", self.check_status())

    # Assign the vehicle
    def assign_vehicle(self):
        if self.available:
            self.available = False
            return "Vehicle assigned successfully"
        else:
            return "Vehicle is already assigned"

    # Return the vehicle
    def return_vehicle(self):
        self.available = True
        return "Vehicle returned successfully"

    # Check availability
    def check_status(self):
        if self.available:
            return "Available"
        else:
            return "Not Available"


# 2. Fleet Class

class Fleet:

    def __init__(self, company_name):
        self.company_name = company_name
        self.vehicles = []

    # Add a vehicle object to the fleet
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    # Show fleet information
    def show_fleet_info(self):
        print("Company:", self.company_name)
        print("Total Vehicles:", len(self.vehicles))

    # Show all vehicles
    def show_all_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.show_info()
            print("--------------------")


# 3. Creating Vehicle Objects

vehicle1 = Vehicle("Toyota Corolla", "DHAKA-1234", "Car")
vehicle2 = Vehicle("Volvo Bus", "DHAKA-5678", "Bus")
vehicle3 = Vehicle("Tata Truck", "DHAKA-9012", "Truck")


# 4. Creating Fleet Object

fleet = Fleet("ABC Transport")


# 5. Adding Vehicles to Fleet

fleet.add_vehicle(vehicle1)
fleet.add_vehicle(vehicle2)
fleet.add_vehicle(vehicle3)


# 6. Showing Fleet Information

fleet.show_fleet_info()

print("====================")


# 7. Showing All Vehicles

fleet.show_all_vehicles()


# 8. Assigning a Vehicle

print(vehicle1.assign_vehicle())
print("Vehicle 1 Status:", vehicle1.check_status())

print("--------------------")


# 9. Trying to Assign the Same Vehicle Again

print(vehicle1.assign_vehicle())

print("--------------------")


# 10. Returning the Vehicle

print(vehicle1.return_vehicle())
print("Vehicle 1 Status:", vehicle1.check_status())