'''

# next-----scopeOfVar.py

scope - it is a region in program where your variable can be accessed and modified.

2 types:
local scope(local variable) : it is defined inside funciton, scope is within function only.
global scope(global variable) : it is defined outside function,
and its scope is anywhere through out program.

'''
# local- variable

def local_var():
    # a is local
    a = 67
    print("Inside function a = ",a)

local_var()
# print("outsides function a = ",a)

# global variable

b = 78

def global_var():
    print("Inside function a = ",b)

global_var()
print("outsides function a = ",b)