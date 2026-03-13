# intro .py after
# 06-03-2026
'''
encapsulation - wrapping up of your data members and member functions in single unit.
hiding of your data
'''
class Employee:

    def __init__(self,name,id,location):
        self.__emp_name = name
        self.__emp_id = id
        self.__location = location

    # def displayInfo(self):
        # print(self.__emp_name,self.__emp_id,self.__location)
    
    # setter and getter method - to modify and access private data member outside class
    # setter method

    def set_name(self,Name):
        self.__emp_name = Name

    def set_id(self,Id):
        self.__emp_id = Id
    
    # getter method
    def get_name(self):
        return self.__emp_name
    
    def get_location(self):
        return self.__emp_id
    
    # pending see lecutre
    # next --->inheritance