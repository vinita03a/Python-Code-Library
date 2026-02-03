# 03-02-2026

'''
Docstring for Datas.py.Opertaors.identity

identity - (is, is not)
compares the memory address of the object
'''

a = [1,2,3]
b = [1,2,3]
c = a

print(a is b)
print(a is c)

# id() - returns the memory address of object
print("id(a) : ",id(a))
print("id(b) : ",id(b))
print("id(c) : ",id(c))