# Created by vidit.singh at 03-03-2022

# Object-oriented programming in python

class Vehicle:
    # This act as a constructor for this class. 'this' keyword is referred to 'self' here. It is mandatory to include
    # self in constructor param. We can access the constructor variable with self in other methods.
    price = '$30000'

    def __init__(self, type_of_vehicle, model):
        self.vehicle_type = type_of_vehicle
        self.model = model

    def display(self):
        print(f'Type of vehicle is {self.vehicle_type} '
              f'and model of the car is {self.model} '
              f'and the price is {Vehicle.price}')


vehicle = Vehicle("car", 'BMW')
print(vehicle.display())
