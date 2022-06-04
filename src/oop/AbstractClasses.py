# Created by vidit.singh at 12-05-2022 By default, Python does not provide abstract classes. Python comes with a
# module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC. ABC works by
# decorating methods of the base class as abstract and then registering concrete classes as implementations of the
# abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.
from abc import ABC, abstractmethod


class Shapes(ABC):
    @abstractmethod
    def my_shape(self):
        pass


class Triangle(Shapes):
    def my_shape(self):
        print("I am Triangle")


class Rectangle(Shapes):
    def my_shape(self):
        print('I am Rectangle')


triangle = Triangle()
print(triangle.my_shape())
