# 17-02-2026
# 14 mock-15 - sunday 16-holiday after intro.py functions

'''
Docstring for Functions.returnstmt


3.non-patameterized return type
4. parameterized return type.

'''

'''
3..non-patameterized return type

Syntax : 

def function_name():
     #block of code
     return expression

var_name = function_name()
print(var_name)
'''

'''
1. Write a function that returns your name.
2. Write a function which returns addition of two numbers
3. Write a function that returns the sum of numbers from 1 to 10.
'''

# 1.

def display_name():
    name = "Vinita"
    return name

# print(dispaly_name())
# OR

output = display_name()
print("Name : ",output)
print(f"My name is {output}, i live in pune.")

print()

#  2.
def addition():
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    return a+b

result = addition()
print("Addition = ",result)

sqr_num = result**2
print("Square or value : ",sqr_num)

# 3

def sum_one_to_ten():
    total = 0
    for i in range(1, 11):
        total += i
    return total

# Main program
print("Sum of numbers from 1 to 10 is:", sum_one_to_ten())


# write a function to check whether number is even or odd

def even_odd():
    n = int(input("Enter a number : "))
    if(n%2==0):
        return True
    else:
        return False
    
if(even_odd()==True):
    print("Even")
else:
    print("Odd")

# write a function to check number is prime or not

def is_prime():
    num = int(input("Enter a number: "))

    if num <= 1:
        return False  # Not prime

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False  # Not prime
    return True  # Prime

# Main program
if is_prime():
    print("The number is prime.")
else:
    print("The number is not prime.")



# or solve by ma'am

def check_prime(n):
    flag = True
    for i in range(2,n):
        if(n%i==0):
            flag = False
            break
    return flag

if(check_prime(5)==True):
    print("is prime")
else:
    print("is not prime.")


'''
4. parameterized return type.

Syntax:
def function_name(parameter):
    # block of code
    return expression

var_name = function_name(argument)
print(var_name)
'''

# write a function to return factorial of a number

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

result = factorial(5)
print("5! = ",result)

# write a function to return area of circle and area of rectangle.

def area(r,l,b):
    aoc = 3.14*r*r
    aor = l*b
    return aoc,aor

result = area(10,6,8)
print(result)
    
r1,r2 = result
print("Area of circle : ",r1)
print("Area of Rec : ",r2)


# write a funciton to check whether a list is palindrome or not.

def palindrome(lst):
   lst1 = lst[::-1]
   if(lst1==lst):
       return True
   else:
       return False
lst = palindrome([1,2,3,3,2,1])
if(lst==True):
    print("palindrome")
else:
    print("not palindrome")
       
'''
1.      Write a function that takes two numbers and returns their sum.
2.      Write a function that accepts two numbers and returns the greater number.
3.      Write a function that takes a string and returns its length.
4.      Write a function that takes a number and returns whether it is even or odd.
5.      Write a function that accepts two numbers and returns their product.
'''

# 1.      Write a function that takes two numbers and returns their sum.
def sum(a,b):
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    sum = a+b
    return sum

result = sum()
print(result)

# 2.      Write a function that accepts two numbers and returns the greater number.
def greater_num(a,b):
    # a = int(input("Enter a number : "))
    # b = int(input("Enter a number : "))
   if(a<b):
    return True
else:
    return False

result = sum()
print(result)