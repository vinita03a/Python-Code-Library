# after inheritance.py
'''
multiple inheritance - one child class inherites properties from more tahn one\
  parent class

P1 , P2 -> C
'''
# parent classs - 1
class Father:
    def show_father(self):
        print("This is class father.")

# parent class -2 
class Mother:
    def show_mother(self):
        print("This is class mother.")

# child class
class Child(Father,Mother):
    def show_child(self):
        print("This is class child")

c = Child()
c.show_child()
c.show_father()
c.show_mother()

# create class to calculate students result

# parent class - 1
class Academics:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def displayAcademics(self):
        print(f"Name : {self.name} , Marks : {self.marks}")

class Sports:
    def __init__(self,score):
        self.score = score
    
    def displayScore(self):
        print(f"Score : {self.score}")

class Result(Academics,Sports):

    def __init__(self, name, marks,score):
        # accessed both parent class constructor
        Academics.__init__(self,name, marks)
        Sports.__init__(self,score)
    
    def ressult(self):
        # pending



# next---->inherit-multilevel.py

# 09-03-2026---method



    