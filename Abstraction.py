# 17-03-2026---after polymorphism

# hiding the implementation details from the user.
# note--- abstract class object we does not create

from abc import ABC,abstractmethod

class Vehicle(ABC):    #abstract class

    @abstractmethod
    def start_engine(self):      #abstract method
        pass

class Car(Vehicle):
    def start_engine(self):
       print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

v1 = Car()
v2 = Bike()

v1.start_engine()
v2.start_engine()



# create the abstract class shape with abstract method area()
# then create a two child class Rectangle, circle each child class should calculate its own area

from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius
    
r = Rectangle(2,6)
print("Area of Rectanlge : ",r.area())

c = Circle(5)
print("Area of Cirlce : ",c.area())
        




