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