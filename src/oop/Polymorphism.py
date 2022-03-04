# Created by vidit.singh at 04-03-2022

# Polymorphism
# Abstract classes

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self, sound):
        raise NotImplementedError("Subclass must implement abstract method!")


class Dog(Animal):

    def speak(self, sound):
        print(f'{self.name} speaks {sound}')


class Cat(Animal):

    def speak(self, sound):
        print(f'{self.name} speaks {sound}')


dog = Dog('Bolt')
print(dog.speak('Bark'))

