#Given 👇🏾, Write a program to determine which class a given Bus object belongs to.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(issubclass(Bus, Vehicle)) #What I did. Appaz, mo shi. Just seeing that I didn't even read the question well.

print(type(School_bus)) #Correction.