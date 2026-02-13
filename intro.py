'''
Docstring for Functions.intro  after comprehension

13-02-2026

function - it is a b;ock of code which executes a certain task only when it is called.

Syntax :
def function_name(parameter):       # variable assigned during function definition
    #  block of code      
       return expression           # return - it ends the function execution and returns
                                      a value to the function
function_name(argument)           # value assigned during function call

use of function:
reusability of code.
to maintain proper structure.

2. types of function
1. user defined function - function created by user 
2. inbuilt function - predefined function 
     examples : print() , len(), input()

4.types of user defined function
1. non-paramterized non return type.
2. parameterized non-return type.
3. non-parameterized return type
4. parameterized return type.
'''

# 1. non-paramterized non return type.



'''
1. write a function to display hello world.
2. Write a function to print your name.
3. Write a function to print numbers from 1 to 10.
4. Write a function to print all even numbers from 1 to 20.
5. Write a function to print the first 5 odd numbers.
'''

# 1.
def dispaly():
    print("Hello world!!")

dispaly()

# 2
def display_name():
    name = "Vinita"
    print("Name : ",name)

display_name()

# 3
def number_range():
    for num in range(1,11):
        print(num)

number_range()

# 4
def even_num():
    for i in range(2,21):
        if(i%2==0):
            print(i,end="")
        print()
even_num()

# 5 
def odd_num():
     for num in range(1,11):
        if(num%2!=0):
            print(num,end="")
        print()
odd_num()

# 2. parameterized non-return type.

# syntax : 
# def function_name(paramter):
    #  block of code

# function_name(argument)

'''
1. Write a function that takes a name as a parameter and prints "Hello <name>".

2. Write a function that takes a number as a parameter and prints whether it is even or odd.

3. Write a function that takes two numbers as parameters and prints their sum.

4. Write a function that takes a string as a parameter and prints its length.

5. Write a function that takes a number n as a parameter and prints the first n natural numbers.
'''

# 1.

def FullName(name):
    print("FullName : ",name)

FullName("Vinita Awhad")

# 2

def check_even(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")
check_even(24)     # n=2

check_even(17)

num = 78
check_even(num)           # n = num

#  3.

# def addition(n1,n2):
#     add = n1+n2
#     print("Addition = ",add)

# n1 = int(input("Enter 1st number :"))
# n2 = int(input("Enter 2nd number :"))
# addition(n1,n2)

# 4
def str_len(s):
    print(len(s))

str_len("Vinita")

# 5
def natural_num(n):
    for i in range(1,n+1):
        print(i)
natural_num(10)


# 6 Write a function to display square of even numbers from given list

def sqr_even_num(lst):
    for i in lst:
        if(i%2==0):
            print(i**2)

num_list = [5, 2,11,13,4,6,19,22,81,18]
sqr_even_num(num_list)

# 7  write a function to display frequency count of an element in given list.

def freq_count(lst):
    count = 0
    for fruit in lst:
        if(fruit=="apple"):
           count += 1
    print(f"apple is repeating {count} times")


fruits = ["apple","banana","apple","cherry","chicoo","jackfruit","banana","apple"]
freq_count(fruits)

# 8  write a function to display frequency count of letter in give string

def freq_letter(s):
    cnt = 0
    for i in s:
        if(i=="a"):
            cnt += 1
    print(f"freq is repeating {cnt}")

s = "python language"
freq_letter(s)
print()

'''
Task:-
1.      Write a function that accepts a number and prints its factorial.
2.      Write a function that accepts a string and prints its reverse.
3.      Write a function that takes a number and prints whether it is even or odd.
4.      Write a function that takes a list of numbers and prints only the even ones.
5.      Write a function that accepts a number and prints its multiplication table.
'''

# 1
 
def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans+=1
    print(f"factorial of {n} is {ans}")
factorial(int(input("enter num ")))

# 2

def reverse_str(s):
    ans = [::-1]
    print(f"")