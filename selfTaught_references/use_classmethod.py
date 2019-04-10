'''
understanding class method

A class method is a method that is bound to a class rather than its object.
It doesn't require creation of a class instance, much like staticmethod.

The difference between a static method and a class method is:

Static method knows nothing about the class and just deals with the parameters
Class method works with the class since its parameter is always the class itself.

'''

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name+' is of age: ', self.age)
        

    
person1 = Person('john', 22)
print(person1.display())

person2 = Person.fromBirthYear('Doe', 1999)
print(person2.display())
