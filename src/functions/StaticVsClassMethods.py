# Created by vidit.singh at 14-05-2022

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# This method is used to return the class object from method. act as factory method.
    @classmethod
    def get_person_object(cls, name, age):
        return cls(name, age)

# This method act as static method.
    @staticmethod
    def is_adult(age):
        return age > 18

    def __str__(self):
        print('name : ', self.name, 'age : ', self.age)


person1 = Person('Vidit', 30)
person2 = Person.get_person_object('Vansh', 2)

print(person1.age)
print(person2.age)
print(Person.is_adult(person2.age))
