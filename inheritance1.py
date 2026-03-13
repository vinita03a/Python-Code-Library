# multiple inheritance------2 parents 1 child
#  ---11-03-2026
'''
Problem Statement: School Management System

A School Management System needs to store information about a student's parents and the student.

A Father class stores the father's details.
A Mother class stores the mother's details.
A Child class should inherit information from both Father and Mother and also store the child’s details.
The system should:

Store the father's name.
Store the mother's name.
Store the child's name.
Display all the information using different methods.

'''
class Father:
    def father_child(self):
        print("This is a father")

class Mother:
    def mother_info(self):
        print("Thsi is a mother")

class Child(Father,Mother):
    def child_info(self):
        print("This is a child")

c = Child()
c.father_child()
c.mother_info()
c.child_info()
    
# using constructor
class Father:
    def __init__(self,father_name):
        self.father_name = father_name
    
    def father_info(self):
        print("Father Name : ", self.father_name)

class Mother:
    def __init__(self,mother_name):
        self.mother_name = mother_name
    
    def mother_info(self):
        print("Mother Name: ",self.mother_name)

class Child(Father,Mother):
    def __init__(self, father_name,mother_name,child):
        super().__init__(father_name)  #calls the father const 
        Mother.__init__(self,mother_name)
        self.child= child
       
    
    def child_info(self):
        print(f"Child name : {self.child}")

c1 = Child("anil","shaila","vin")
c1.father_info()
c1.mother_info()
c1.child_info()

'''
Problem Statement: Smart Device System

A company is designing a Smart Device System.

A Camera class provides camera features.
A MusicPlayer class provides music playing features.
A SmartPhone class should inherit features from both Camera and MusicPlayer.
The system should allow the smartphone to:

Take photos using camera functionality.
Play music using music player functionality.
Store the smartphone model name.
Since the SmartPhone needs features from both Camera and MusicPlayer, we use multiple inheritance.

'''

# class Camera:
#     def __init__(self,c_feature):
#         self.c_feature = c_feature

#     def camera_info(self):
#         print("Camera feature : ", self.c_feature)

# class MusicPlayer:
#     def __init__(self,m_feature):
#         self.m_feature = m_feature

#     def music_info(self):
#         print("Music feature : ", self.m_feature)
    
# class SmartPhone(Camera,MusicPlayer):
#     def __init__(self, c_feature,m_feature,model_name):
#         super().__init__(c_feature) 
#         MusicPlayer.__init__(self,m_feature)
#         self.model_name = model_name
       
    
#     def smartphone_info(self):
#         print("SmartPhone model  : ",self.model_name)

# s = SmartPhone("64MP ","MPQ3","Apple")
# s.camera_info()
# s.music_info()
# s.smartphone_info()


##########################################

# multilevel
# Grandparent -> Parent -> Child

# class Grandparent:
#     def grandparent_info(self):
#         print("This is a grandparent")

# class Parent(Grandparent):
#     def parent_info(self):
#         print("This is a parent")

# class Child(Parent):
#     def child_info(self):
#         print("This is a child")

# c2 = Child()

# c2.grandparent_info()
# c2.parent_info()
# c2.child_info()


# using constructor

# class Grandparent:
#     def __init__(self,gname):
#         self.gname = gname
#     def grandparent_info(self):
#         print("This is a grandparent : ",self.gname)

# class Parent(Grandparent):
    
#     def __init__(self,gname,pname):
#         def ___init_(self,gname,pname):
#              super().__init__(gname)
#              self.pname = pname


#     def grandparent_info(self):


#     def parent_info(self):
#         print("This is a parent")

# class Child(Parent):
#     def child_info(self):
#         print("This is a child")

# c2 = Child()

# c2.grandparent_info()
# c2.parent_info()
# c2.child_info()
# # agina write lecuter



# 

# class Grandparent:
#     def grandparent(self,Gname):
#         self.Gname = Gname
#     def g_info(self):
#         print("This is a grandfather")

# Hierarchical Inheritance 1 parent multiple child
# class Parent:
#     def parent_info(self):
#         print("This is a parent")

# class Child1(Parent):
#     def child1_info(self):
#         print("This is a child 1")

# class Child2(Parent):
#     def child2_info(self):
#         print("This is a child 2")

# a = Child1()
# b = Child2()
# a.parent_info()
# a.child1_info()

# b.parent_info()
# b.child2_info()


# using constructor
# class Parent:
#     def __init__(self,parent_Name):
#         self.ParentName = parent_Name

#     def 




# 13-03-2026
# hybrid inheritance (combination of single multiple nad multilevel)
class A:
    def displayA(self):
        print("This is a class A")

class B(A):
    def displayB(self):
        print("This is a class B")

class C:
    def displayC(self):
        print("This is a class C")

class D(C,B):
    def displayD(self):
        print("This is a class D")

d1 = D()
d1.displayA()
d1.displayB()
d1.displayC()
d1.displayD()


# constructor
class A:
    def __init__(self,a):
        self.a = a
    def displayA(self):
        print("This is a class A")

class B(A):
    def __init__(self,a ,b):
        super().__init__(a)   #calling  A constructor
        self.b = b
    def displayB(self):
        print("This is a class B",self.b)

class C:
    def __init__(self,c):
        self.c =c
    def displayC(self):
        print("This is a class C",self.c)

class D(C,B):
    def __init__(self,c,a,b,d):
        B.__init__(self,a,b)
        C.__init__(self,c)
        self.d = d

    def displayD(self):
        print("This is a class D",self.d)

d1 = D(10,20,30,40)
d1.displayA()
d1.displayB()
d1.displayC()
d1.displayD()


# next topic is polymorphism