#Given
from os import sep


class Vehicle:
    
    color = 'white' #My addition. Lol, my commenting is cringe af.

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

"""
Define a class attribute ”color” with a default value white. I.e., Every Vehicle should be white.
"""

""""
Expected Output
Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
"""

#Testing

school_volvo = Vehicle('School Volvo', 180, 12)
audi_Q5 = Vehicle('Audi Q5', 240, 18)

#Do I still know lists?
car_list = [school_volvo, audi_Q5]

for car in car_list:
    print('Color : ', car.color, ', Vehicle name : ', car.name, ', Speed : ', car.max_speed, ' Mileage : ', car.mileage, sep='')