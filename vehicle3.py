#Given
class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

"""
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
"""

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

car = Bus('Volvo', 240, 56)
print("Vehicle Name:", car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
