# 03-02-2026

'''
Docstring for Conditionals.nestedif

Syntax :
if(condition):
    #block of code
    if(condition):
        #block of code
    else:
      #block of code
else:
    if(condition):
        #block of code
    else:
       #block of code
'''

'''
    1. Check if a number is positive, then check if it is even or odd.
    2. Write a Python program using nested if-else to check student's result:
        Marks < 40 → Fail, 40-74 → Pass, ≥75 → Pass with Distinction. do it.
    3. Login system: check username, then check password.
    4. Greatest among three numbers.
    5. Check if a number is divisible by 2, then check divisibility by 4.
    6. Find the smallest of 3 nos using nested if-else
'''


# # 1.Check
# n = int(input("Enter a number : "))
# if(n>0):
#     print("numbe is positive.")
#     if(n%2==0):
#         print("number is even")
#     else:
#         print("number is odd.")
# else:
#     print("number is negative")





# 2
# Program to check student's result using nested if-else

def check_result(marks):
    """Check and print student's result based on marks."""
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter a value between 0 and 100.")
    else:
        if marks >= 40:  # Pass condition
            if marks >= 75:
                print("Result: Distinction")
            elif marks >= 60:
                print("Result: First Class")
            elif marks >= 50:
                print("Result: Second Class")
            else:
                print("Result: Pass Class")
        else:
            print("Result: Fail")

# Main program
try:
    marks = float(input("Enter student's marks (0-100): "))
    check_result(marks)
except ValueError:
    print("Invalid input! Please enter a numeric value.")


# # 3 Login system: check username, then check password.

# username = input("Enter username : ")
# password = input("Enter password : ")

# if(username=="vinita@gmail.com"):
#     if(password=="vinita123"):
#          print("Login Successfull!!")
#     else:
#         print("Invalid password!!")
# else:
#     print("Invalid username!!")

# 4. Greatest among three numbers.

# 5
# Program to check divisibility by 2 and then by 4

def check_divisibility(num):
    # First check divisibility by 2
    if num % 2 == 0:
        print(f"{num} is divisible by 2.")
        
        # Now check divisibility by 4
        if num % 4 == 0:
            print(f"{num} is also divisible by 4.")
        else:
            print(f"{num} is NOT divisible by 4.")
    else:
        print(f"{num} is NOT divisible by 2, so no need to check for 4.")

# Main program
try:
    # Take user input
    number = int(input("Enter an integer: "))
    check_divisibility(number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# 6


# calculator program

n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))

optr = input("Enter operator : ")

if(optr =='+'):
  print("Addition : ", n1+n2)
elif(optr =='-'):
  print("Subtraction : ", n1-n2)
elif(optr =='/'):
    if(n2==0):
         print("Cannot divide by zero.")
    else:
        print("Division :",n1/n2)
else:
    print("Invalid operator chosen.!!")


    # 04-02-2026

    '''
   match case 


it selects one of many block of codes for execution.
it has multiple cases, on basisi of which it selects block of code
it executes a block of code where expression matches a case

Syntax : 
match expression:
    case value1:
        # block of code
    case value2:
        # black of code
    case value3:
        # block of code
    .
    .
    .
    case _:               # default case
        # block of code

    Syntax : 
    match express

    '''


    '''
   1. Write a program that takes an operator symbol (+, -, *, /) and performs the 
corresponding operation on two numbers.
2. Write a program that asks for a shape (circle, square, rectangle) and calculates 
its area using match-case.
    '''

    # 1
    n1 = int(input("Enter number 1 : "))
    n2 = int(input("Enter number 2 : "))

    optr =int(input("Enter number operator : "))

    match optr :
        case'+':
            print("Addition = ",n1+n2)
        case'-':
            print("Subtraction = ",n1-n2)
        case'*':
            print("Product = ",n1*n2)
        case'/':
            if(n2==0):
                print("Cannot divide by zero = ")
            else:
                print("Division = ,n1/n2")
        case _:
            print("Please enter from given option!!")

        
    # 2 Write a program that asks for a shape (circle, square, rectangle) and calculates 
    #   its area using match-case.

n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
   

'''
 using pip operator (|) - (like logical or operator)
 we use pip optr to execute same block of code for multiple cases.
# check on the basis of condition or values i.e diff from if-else 
   '''

# to describe a day is weekday or weekend

day = int(input("Enter day number : "))

match day:
    case 1|2|3|4|5:
        print("Weekday")
    case 6|7:
        print("Weekend.")
    case _:
        print("Invalid day number.")

'''
using if in match case

'''
#  to check a number as a positive negative or zero


n = int(input("Enter day number : "))

match n:
    case n if n>0:
        print("Positive.")
    case n if n<0:
         print("Negative.")
    case n if 0:
         print("Zero entered")
         

# check if number is even or odd

num = int(input("Enter a number : "))

match num%2==0:
    case 0:
         print("even")
    case 1:
        print("odd")



