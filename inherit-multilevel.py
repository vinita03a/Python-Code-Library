# next-->multileve.py
# 6-03-2026

'''
multilevel - one child class inherits from parent class, parent class inherits from grand parent
 GP -> P -> C
'''
class GrandParent:
    def show_gp(self):
        print("This is GP class.")

class Parent(GrandParent):
    def show_parent(self):
        print("This is parent class.")

class Child(Parent):
    def show_child(self):
        print("This is child class.")

c = Child()
c.show_child()
c.show_parent()
c.show_gp()

print("-"*30)

# GP class
class Student:
    def __init__(self,name):
        self.name = name

    def studentInfo(self):
        print("Student name : ",self.name)

# Parent
class Exam(Student):
    def __init__(self, name, mark1,mark2,mark3):
        super().__init__(name)
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def total_marks(self):
        total = self.mark1+self.mark2+self.mark3
        return total
    
# child

class Result(Exam):
    def __init__(self, name, mark1, mark2, mark3):
        super().__init__(name, mark1, mark2, mark3)
        
    def result(self):
        total = super().total_marks()
        avg = total/3
        print("Avg = ",avg)
        if(avg>=75):
            print("student is passed by distinction.")
        elif(avg>=40 and avg<=75):
            print("Passed.")
        else:
            print("Failed")

r1 = Result("kriti",45,67,81)
r1.studentInfo()
print(r1.total_marks())
r1.result()

