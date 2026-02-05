# Skip to main content
# Home
# Calendar
# Archived classes
# Settings
# 1.Take your name as input and print:
# 	o/p - Hello, <name>! Welcome to Python.

name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Python.")



# 2.Take your age as input and print:
# 	o/p - You are <age> years old. Next year, you will be <age+1>.


age = int(input("Enter your age: "))
print(f"You are {age} years old. Next year, you will be {age + 1}.")


# 3.Take length and width as input and print:
# 	o/p - The area of rectangle with length <length> and width <width> is <area>.

length = int(input("Enter your length: "))
width =  int(input("Enter your width: "))
area  = length*width

print(f"The area of rectangle with length {length} and width {width} is {area}")



# 4.Take radius as input and print:
# 	o/p - The circumference of a circle with radius <r> is <2 * 3.14 * r>.
r = int(input("Enter your  radius: "))
print(f"The circumference of a circle with radius {r} is {2 * 3.14 * r}.")


# 5.Take first name and last name as input and print:
# 	o/p - Your full name is <firstname lastname>.
firstname = input("Enter your  firstname: ")
lastname = input("Enter your  lastname: ")
print(f"Your full name is {firstname} {lastname}.")

# 6.Take principal, rate, and time as input and print:
# 	o/p - Simple Interest for principal <P>, rate <R>% and time <T> years is <SI>.
P = int(input("Enter your  principal: "))
R = int(input("Enter your  rate: "))
T = int(input("Enter your  time: "))
SI = (P*R*T)/100
print(f"Simple Interest for principal {P}, rate {R}% and time {T} years is {SI}")

# 7.Take Celsius as input and print:
# 	o/p - <C>°C is equal to <F>°F.
# (Formula: F = (C*9/5) + 32)

C = int(input("Enter your  rate: "))
F = (C*9/5) + 32
print(f"{C}°C is equal to {F}°F.")


# 8.Take marks in 5 subjects as input and print:
# 	o/p - You scored <percentage>% in total.

Maths = float(input("Enter your  Maths: "))
Eng = float(input("Enter your  Eng: "))
Hindi= float(input("Enter your  Hindi: "))
Sci  = float(input("Enter your  Sci: "))
Social =float(input("Enter your  Social: "))

total_marks = Maths + Eng + Sci + Hindi+ Social
max_marks = 5 * 100

percentage = (total_marks / max_marks) * 100

print(f"You scored {percentage} % in total.")

# 9.Take item name, quantity, and price per unit as input and print:
# 	o/p - The total cost for <quantity> <itemname>(s) at Rs.<price> each is Rs.<total>.

itemname = input("Enter your  itemname: ")
quantity = int(input("Enter your  quantity: "))
price =  float(input("Enter your  quantity: "))

total = quantity*price

print(f"The total cost for {quantity} {itemname}(s) at Rs.{price} each is Rs.{total}")

# 10.Take a number as input and print:
# 	o/p - The square of <n> is <n**2> and the cube is <n**3>.

n =  int(input("Enter your  number: "))
print(f" The square of {n} is {n**2} and the cube is {n**3}.")


# 11.Take a number as a string input and convert it into an integer. Print its square.

n =  int(input("Enter your  number: "))
print(f"its square is {n*n}")

# 12.Take an integer input and convert it to float. Print both values.

x =  int(input("Enter your  number: "))

print(f"{x}, type-{type(x)}")

x_float = float(x)
print(f"{x_float}, type-{type(x_float)}")

# 13.Take a decimal number input and convert it into an integer. Print both values.

x = 45
print(f"{x}, type-{type(x)}")

# 14.Take a number as input and convert it into a string. Print "The number is <num>" using f-string.
number = "36"
print(f"{number}, type-{type(number)}")


# 15.Take two numbers as string input. Convert them into integers and print their sum.

num1 = "56"
num2 = "12"
add = int(num1)+int(num2)
print(add)

# 16. Create a variable name with your name and print:
# My name is <name>

name = "Vinita"
print(f"My name is {name}")

# 17. Store your age in a variable and print:
# I am <age> years old.
age = input("Enter age: ")
print(f"I am {age} years old.")


# 18. Store two numbers in variables a and b. Print their sum.

a = 20
b = 30
sum=a+b 
print(f"{sum}")


# 19. Store the value of π = 3.14159 in a variable and print:
# Value of π is 3.14159
π = 3.14159
print(f"Value of {π}")


# 20. Create a variable country with your country name and print:
# I live in <country>

country = input("Enter country name : ")
print(f"I live in {country}")

# 21. Store two strings in variables and print them together as a sentence.
first = "lily"
last = "jonas"

print(f"{first} {last}")


# 22. Store marks of 3 subjects in variables and print the total.

num1 = 78
num2 = 56
num3 = 40
total = (num1+num2+num3)/3

print(f"total marks of 3 subjects {total}")


# 23. Assign True to a variable and print its type using type().
variable = True
print(type(variable))

# 24. Store a float number in a variable and print:
num = 23.5

print("float number is = ",num)

# The number is <value>
# Assignment - Basics.txt
# Displaying Assignment - Basics.txt.