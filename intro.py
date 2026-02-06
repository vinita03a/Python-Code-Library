# 03-02-2026
'''
Docstring for Conditionals.intro

Conditional statement - these are the statements which executes a block of code on the basis of condition applied.

types:
1. if
2. if else
3. if elif else
4. nested if else
5. match case
'''

'''
if statement

Syntax:
if(condition):
    #block of code
'''

x = 67
if(x>50):
    print("is greater.")

# age criteria

age = int(input("Enter age to check eligibility : "))
if(age>18):
    print("can vote.")