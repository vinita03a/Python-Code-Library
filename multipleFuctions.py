'''
18-02-2026 after 4.parameterized


multiple function - creating many function in single script
'''
# #  1.
# def add(a,b):
#     return a+b

# def sub(a,b):   #return
#     return a-b

# result1 = add(9,7)  #call
# print("Addition = ",result1)


# result2 = sub(15,7)
# print("Subraction = ",result2)

# product = result1*result2
# print("Product = ",product)


# '''
# 1  Write two functions:

#     add(a, b) → returns sum

#     subtract(a, b) → returns difference

# 2  Write a function square(n) that returns square of a number, and another cube(n) that returns cube. do it

# 3  Write a function is_even(n) to check even number, and another function that prints all even numbers from 1 to 20 using it.


# '''

# # 3.

# def is_even(n):
#     return n%2==0

# def display_even():
#     for i in range(1,21):
#         if(is_even(i)==True):
#             print(i)

# display_even()

# 2.
# def sqr(n):
#     return n**2

# def cube(n):
#     return n**3

# num = sqr(5)
# print("square is ",sqr) 

# num = cube(5)
# print("cube is ",cube) 



# print("-------------------Menu Driven Program-----------------------")

# # Menu driven program

# def addition(x,y):
#     return x+y

# def subtraction(x,y):
#     if(x<y):
#         x,y = y,x
#         return x-y
#     return x-y

# def division(x,y):
#     if y==0:
#         return f"Cannot divide by zero!!"
#     else:
#         return x/y
    
# def product(x,y):
#     return x*y

# print("Calculator:\n1.Addition.\n2.Subtraction.\n3.Division.\n4.Product.\n5.Exit")
# option  = int(input("Enter an option 1/2/3/4/5 : "))

# n1  = int(input("Enter 1st number : "))

# n2  = int(input("Enter 2nd number : "))

# if(option == 1):
#     n1  = int(input("Enter 1st number : "))

#     n2  = int(input("Enter 2nd number : "))
#     result = addition(n1,n2)
#     print("addition : ",result)

# elif (option == 2):
#     n1  = int(input("Enter 1st number : "))

#     n2  = int(input("Enter 2nd number : "))
#     result = subtraction(n1,n2)
#     print("subtraction : ",result)
    
# elif (option == 3):
#     n1  = int(input("Enter 1st number : "))

#     n2  = int(input("Enter 2nd number : "))
#     result = division(n1,n2)
#     print("division : ",result)

# elif (option == 4):
#     n1  = int(input("Enter 1st number : "))

#     n2  = int(input("Enter 2nd number : "))
#     result = product(n1,n2)
#     print("product: ",result)

# elif(option == 5):
#     print("Exit!!")




# print()
# print("-",40)

# # # Program should keep asking to choose option until user chooses exit option.

# def addition(x,y):
#     return x+y

# def subtraction(x,y):
#     if(x<y):
#         x,y = y,x
#         return x-y
#     return x-y

# def division(x,y):
#     if y==0:
#         return f"Cannot divide by zero!!"
#     else:
#         return x/y
    
# def product(x,y):
#     return x*y

# print("Calculator:\n1.Addition.\n2.Subtraction.\n3.Division.\n4.Product.\n5.Exit")
# option  = 0

# while(option!=5):
#     option  = int(input("Enter an option 1/2/3/4/5 : "))
#     if(option==1):
#         result = addition(10,5)
#         print("Addition = ",result)
#     elif(option==2):
#         result = subtraction(8,17)
#         print("Subtraction = ",result) 
#     elif(option==3):
#         result = product(18,0)
#         print("Product = ",result) 
#     elif(option==4):
#         result = division(19,15)
#         print("Division = ",result)
#     elif(option==5):
#         print("Exit!!")
#         break

# write a menu driven program which gives factorial of a number, and gives square of number and finds a number is palindrome or not.


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact



def sqr(n):
    return n**2 

def palindrome(n):
   n = n[::-1]
   if(n==n):
       return True
   else:
       return False




num = factorial(5)
print("5! = ",factorial)  
num = sqr(5)
print("square is ",sqr)

num = palindrome(55)
print("Palindrome is  :",palindrome)

print("Calculator:\n1.Addition.\n2.Subtraction.\n3.Division.\n4.Product.\n5.Exit")
option  = 0

while(option!=5):
    option  = int(input("Enter an option 1/2/3/4/5 : ")).
    
    if(option==1):
        result = addition(10,5)
        print("Addition = ",result)
    elif(option==2):
        result = subtraction(8,17)
        print("Subtraction = ",result) 
    elif(option==3):
        result = product(18,0)
        print("Product = ",result) 
    elif(option==4):
        result = division(19,15)
        print("Division = ",result)
    elif(option==5):
        print("Exit!!")
        break