# 02-02-2026
'''
Docstring for Datas.py.Opertaors.logical

Logical operator - (and, or ,not)
combining more than one condition, logical operator performs operation on it and returns True an False
'''

'''
Truth table
and
T and T : T
T and F : F
F and T : F
F and F : F


OR 
T or T : T
T or F : T
F or T : T
F or F : F

not 
not T : F
not F : T

'''

a = 56 
b = 72
c = 45 
d = 56

print(a>b and c==a)   # F and F : F 
print(c>=d and a==d)  # F and T : F


# a number is positive as well as even

x = int(input("Enter a number : "))
print(x>0 and x%2==0)


print(c>=d or a==d) # F or T : T

 # a number should be either positive or even---apply or operator

x = int(input("Enter a number : "))
print(x>0 or x%2==0)


# print(not c<=d) # not T : F

print(not(a == d or b<=c )) # not(T and F) : not (T) : F