# 03-02-2026
'''
Docstring for Conditionals.ifelifelse

if elif else - used when we need multiple conditions to apply.

Syntax :
if(condition):
    #block of code
elif(condition):
    #  block of code

-
-
-
else:
     #block of code
'''


'''
1.  Classify a number as positive, negative, or zero.
2.  Classify a character as vowel, consonant, or other.
3.  Classify age into child (<13), teenager (13-19), or adult (20+).
4.  Check if a number is divisible by 2, 3, or neither.
5.  Classify a day number (1-7) into weekday or weekend.
6.  Classify marks into grades: A (≥90), B (≥75), C (≥50), F (<50).
7. Enter a number (1-7) and print the day name. If not in range, print "Invalid".
8. Input color ("red", "yellow", "green") and print "Stop", "Get Ready", or "Go". Otherwise, print "Invalid Color".
9. Input a year. Print "Leap Year", "Not Leap Year", or "Invalid input" (for negative years).
    (Rule: divisible by 4 but not by 100, except divisible by 400).
10.Input two numbers and an operator (+, -, *, /). Use if-elif to perform the correct operation.
'''

# 1 Classify a number as positive, negative, or zero.

# n = int(input("Enter a number : "))
# if(n>0):
#     print("number is positive")
# elif(n<0):
#     print("number is negative.")
# else:
#     print("number is zero")

# # 2. Classify a character as vowel, consonant, or other.


# char = input("Enter a character : ")
# vowel = "aeiouAEIOU"

# if(char in vowel):
#     print("Character is vowel.")
# elif(char.isalpha() and char not in vowel):
#     print("Character is consonant.")
    
# else:
#     print("other.")

# #3.  Classify age into child (<13), teenager (13-19), or adult (20+).

# age = int(input("Enter age : "))
# if(age<13):
#     print("Child")

# elif(age>=13 and age<=19):
#     print("Teenager.")
# else:
#     print("Adult.")


# 4.  Check if a number is divisible by 2, 3, or neither.
number = int(input("Enter the number : "))
if(number%2==0):
    print("divisible by 2")
elif(number%3==0):
    print("divisible by 3")
else:
    print("neither")

# 5.  Classify a day number (1-7) into weekday or weekend.

day = int(input("Enter a day number : "))

if(day==1 or day==2 or day==3 or day==4 or day==5):
    print("Weekday.")
elif(day==6 or day==7):
    print("Weekend")
else:
    print("Please enter valid day number!!!")
    
# 6. Classify marks into grades: A (≥90), B (≥75), C (≥50), F (<50).
# 7. Enter a number (1-7) and print the day name. If not in range, print "Invalid".
# 8. Input color ("red", "yellow", "green") and print "Stop", "Get Ready", or "Go". Otherwise, print "Invalid Color


'''
9. Input a year. Print "Leap Year", "Not Leap Year", or "Invalid input" (for negative years).
    (Rule: divisible by 4 but not by 100, except divisible by 400).
'''

year = int(input("Enter a year : "))
if(year<0):
    print("Invalid input")
elif(year%400==0 or (year%4==0 and year%100!=0)):
    print("Leap year.")
else:
    print("Not leap year.")


# 10.Input two numbers and an operator (+, -, *, /). Use if-elif to perform the correct operation.

# calculator

print("Calculator:\n1.Addition(+).\n2.Subtraction(-).\n3.Multiplication(*).\n4.Division(/) : ")

n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))

option = int(input("Enter an operator : "))

if(option=='+'):
    print("Addition = ",n1+n2)
elif(option=='-'):
    print("Subtraction = ",n1-n2)
elif(option=='*'):
    print("Product = ",n1*n2)
elif(option=='+'):
    print("Addition = ",n1+n2)