# Created by vidit.singh at 19-05-2022

class Person:
    address = 'Noida' # Class variable

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    def show_employee(self):
        print(f'Employee name is {self.name} and age {self.age} lives in {self.address}')


person = Person("Vansh", 2)
person2 = Person("Hritik", 20)

person.show_employee()
person2.show_employee()

person.address = "Delhi"  # this only changes the address object of that object not class level object.
person.show_employee()

Person.address = 'Mumbai'
print(person.address)
print(person2.address)
print(Person.address)
