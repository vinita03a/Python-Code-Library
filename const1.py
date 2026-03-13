# 10-03-2026

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name : {self.name}, Age: {self.age}")

s1 = Student("Alice",20)
s1.show()

# parameterized 
# car ki price or brand print
class Car:
    def __init__(self,price,brand):
        self.price = price
        self.brand = brand    #instance variable declare

    def show(self):
        print(f"Brand: {self.brand}, Price: {self.price}")
c = Car(500000, "Toyato")
c.show()

# non parameterized const
class Student:
    def __init__(self):
        self.name = "Unknown"
        self.age =0
    
    def display(self):
        print(f"Name : {self.name}, Age:{self.age}")
    
s2 = Student()
s2.display()

# single inheritance (only methods)
# single child class inherit the single parent class
class Person:
    def display(self):
        print("I am a person")

class Student(Person):
    def study(self):
        print("I am studying")

s3 = Student()
s3.display()
s3.study()

# with constructor
class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"I am {self.name}")

class Student(Person):
    def __init__(self, name,course):
        super().__init__(name)    #calling parents
        self.course = course

    def study(self):
        print(f"I am {self.course}")

s4 = Student("Alice","Python")
s4.display()
s4.study()

# # A company wants to create a Python program to manage employee information.

# Create a parent class Employee that stores the employee's name and salary using a constructor.

# The class should also have a method to display employee details.

# Create a child class Manager that inherits from the Employee class.

# The Manager class should add an additional attribute department using its constructor.

# It should also have a method to display the manager's department.


class Employee:
    def __init__(self,ename,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee details : {self.name}, Salary : {self.salary}")

class Manager(Employee):
    def __init__(self, ename,salary, department):
        super().__init__(ename,salary)    #calling parents
        self.department = department

    def details(self):
        print(f"Manager's department: {self.department}")

d1 = Manager("Ovi",25000,"IT")
d1.display()
d1.details()

# next--multiple--inheritance1.py
