# 09-03-2026
# akshay sir ---after inherit multiple.py
# methods
class Student:
    def greet(self):
        print("I am a student")

s1 = Student()
s1.greet()

# instance method---call with obj
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def show(self):   #instance method
        print(f"Name : {self.name}, Marks : {self.marks}")

s1 = Student("Alice", 90)

s1.show()


# class level method
class Student:
    school = "ABC School"    # class variable

    @classmethod
    def get_school(cls):
        print(f"School Name : {cls.school}")

# call using class
Student.get_school()