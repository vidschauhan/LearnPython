# Created by vidit.singh at 03-03-2022
# Inheritance
class Animal:
    breed = 'No Breed'

    def __init__(self):
        print("Instance of Animal created!")

    def who_am_i(self):
        print('I am an Animal!')

    def get_type(self, animal_type):
        print(f'My type is {animal_type}')

    def get_breed(self, breed):
        print(f'My breed is {breed}')


class Dog(Animal):

    def __init__(self):
        super().__init__()  # Calling Immediate Parent Class constructor.

    def who_am_i(self):
        print('I am dog')

    def get_sound(self, sound):
        print(f" I sound like {sound}")

    def get_type(self, animal_type):
        print(f'My type is {animal_type}')

    def get_breed(self, breed):
        print(f'My breed is {breed}')


dog = Dog()
print(dog.get_breed(breed='Lab'))