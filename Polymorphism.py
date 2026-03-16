# 13-03-2026  after hybrid inheritance

# compile time polymorphism(method overloading)
# same class , same method but different parameter

# eg
class Calculator:
    def add(self,a,b = 0,c = 0):
        return a+b+c
cal = Calculator()
print(cal.add(2))
print(cal.add(2,3))
print(cal.add(2,2,2))


#  food ordered system
class FoodOrder:
    def order(self,item1, item2=0, item3 = 0):
        print(item1+item2+item3)

f = FoodOrder()
f.order(100)
f.order(100,150)
f.order(100,100,100)



# method overriding (run time poly)
# differnt class name , same method , same parameter

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog makes sound")

class Cat(Animal):
    def sound(self):
      print("Cat makes a sound")


d1 = Dog()
c2 = Cat()
d1.sound()
c2.sound()


# 16-03-2026---14/15---holiday
# method overriding

# Problem statement:
# Create a base class Vehicle with a method show_speed().
# Create  subclasses Car and Bike that override this method

class Vehicle:
   def show_speed(self):
       print("Vehicles has a different spped")
         
class Car(Vehicle):
    def show_speed(self):
        print("Car has a speed 120km/h")

class Bike(Vehicle):
    def show_speed(self):
        print("Bike has a speed 80km/h")

v1 = Car()
v2 = Bike()

v1.show_speed()
v2.show_speed()


# Q.Problem statement:
# Create a base class Notification with method send().
# Override it in EmailNotitification ,SMSNotification ,PushNotification 

class Notification:
   def send(self):
       print("sending the Notifications...")
         
class EmailNotitification(Notification):
    def send(self):
        print("send the Email Notification")

class SMSNotification(Notification):
    def send(self):
        print("send the SMS Notification")

class PushNotification(Notification):
    def send(self):
        print("sending the Push Notification")

N1 = EmailNotitification()
N2 = SMSNotification()
N3 = PushNotification()

N1.send()
N2.send()
N3.send()

#  Create a base class Person with a constructor that initialize the name.
# Create a derived class Student that inherits from Person, uses the Constructor, course , override a method.
class Person:
    def __init__(self,name ):
        self.name = name
        print("Person const is called ")

    def show(self):
        print("Name : ",self.name)

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
        print("Child class constructor called")

    def show(self):
        print("StudentName :",self.name)
        print("Course : ",self.course)

s1 = Student("Vinita","Data Science")
s1.show()


'''
Problem Statement:

Create a base class Shape with a constructor that initializes the shape name.

Create two derived classes Rectangle and Circle.

Requirements:

Use a constructor (__init__) to initialize values like length, width, or radius.
Override the method area() in both classes.
Rectangle should calculate area using length × width.
Circle should calculate area using π × radius × radius.
Demonstrate runtime polymorphism by calling the area() method for different objects.

'''
class Shape:
    def __init__(self,name ):
        self.name = name

    def area(self):
        print("Area calculations")

class Rectangle(Shape):
    def __init__(self, length,width):
        super().__init__("Rectangle")
        self.width = width
        self.length = length 

    def area(self):
        print("area of Rectangle : ",self.length * self.width)

class Circle(Shape):
    def __init__(self , radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        print("area of Circle : ",3.14 * self.radius * self.radius)


r = Rectangle(5,4)
c = Circle(3)

r.area()
c.area()








