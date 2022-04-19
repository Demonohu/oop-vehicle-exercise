class  Vehicle:

    """
    Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
    """

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
benz = Vehicle(180, 12)
print('I have a Benz and the speed is', benz.max_speed, 'and the mileage is', benz.mileage)