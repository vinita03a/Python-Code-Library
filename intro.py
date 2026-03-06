'''
after file handling
05-03-2026

Object Oriented Programming

its a programming structure which uses classes and objects

# focuses on structure

OOPs principles : 

1. class

2. object

3. Encapsulation

4. Inheritance

5. Polymorphism

6. Abstraction

1. class - blueprint/template of an object
    it is collection of data members and member functions
2. object - instance of a class
'''

# create a class

class Myclass:
    x = 7

# create an object 

obj = Myclass()
print(obj.x)  

'''
Syntax :
class classname:
    # constructor - function which is called when an object is created.
    # use - to declare instance variables
    def __init__(self):
        #data members/instance variables/attributes
    
    # member functions/instance methods/methods
    def function_name(self):
        # code

# create an object 
obj = classname() -> constructor is called here

# self parameter - this defines instance variables, and also used to access data members and member functions through out class.


'''
# note---it is non parameterized constructor based

# create a class to calculate area of circle

# class AreaOfCircle:
#     # constructor
#     def __init__(self):
#         # data member
#         self.radius = 5

#     # member function
#     def AOC(self):
#         print("Area of circle = ",3.14*self.radius*self.radius)

# aoc = AreaOfCircle()    #create object
# aoc.AOC()


# parameterized constructor

class AreaOfCircle:

    def __init__(self,r):
        self.radius = r

    def AOC(self):
        print("Area of circle : ",3.14*self.radius*self.radius)

aoc1 = AreaOfCircle(10)
aoc1.AOC()

aoc2 = AreaOfCircle(6)
aoc2.AOC()

# create a class Students for students information

class Students:

    # constructor
    def __init__(self,name,age,marks1,marks2):
        self.s_name = name
        self.s_age = age
        self.s_marks1 = marks1
        self.s_marks2 = marks2

    def displayInfo(self):
        print("Students name : ",self.s_name)
        print("Students age : ",self.s_age)
        print("Students marks1 : ",self.s_marks1)
        print("Students marks2 : ",self.s_marks2)

    def total_marks(self):
        total = self.s_marks1 + self.s_marks2
        print("Total marks = ",total)

s1 = Students("Disha",24,78,91)
print("---------------Student-1 details as below:------------------")
s1.displayInfo()
s1.total_marks()


s2 = Students("Nishu",21,89,79)
print("---------------Student-2 details as below:------------------")
s2.displayInfo()
s2.total_marks()

# create a class Employee which accepts data members from user

class Employee:

    def __init__(self):
        self.emp_name = ""
        self.emp_id = 0
        self.emp_rating = 0.0

    def AcceptData(self):
        self.emp_name = input("Enter emp name : ")
        self.emp_id = int(input("Enter emp id : "))
        self.emp_rating = float(input("Enter emp rating : "))

    def DisplayData(self):
        print("Emp name = ",self.emp_name)
        print("Emp id = ",self.emp_id)
        print("Emp rating = ",self.emp_rating)

e1 = Employee()
print("---------Enter Employee details below--------")
e1.AcceptData()
print("--------- Employee Details is shown below--------")
e1.DisplayData()

# Create a class Arithmetic having a constructor for variables and 3 functions

# for add,sub,div and create 2 objects of a class Arithmetic.

'''
Write a Python program to create a class Book.

Requirements:
- Data members: title, author, price
- Method accept() → take values from user
- Method display() → print book details
- Create object and call methods

 

Write a Python program to create a class Rectangle.

Requirements:
- Constructor should take length and width
- Method area() → returns area
- Method perimeter() → returns perimeter
- Create object and print area and perimeter

'''

# do it---check grp

# next--encapsulation

