'''
after menu driven option
18-02-2025
'''
'''
lambda funciton - its an anonymous function, which performs a small task in single line of expression

Syntax :
lambda parameter : expressions

you can have multiple parameters, but only single expression

'''

# add = lambda n1,n2 : n1+n2
# print("Addition = ", add(14+18))
# print(type(add))

# sub = lambda a,b : print("Subtraction = ",a-b)
# sub(19,7)

'''
1. Write a lambda function to display square of a number.

2. Write a lambda function to check if number is even or odd.

3. Write a lambda function to add 10 to a number.

4. Write a lambda function to find the maximum of two numbers.

5. Write a lambda function to find the minimum of two numbers.   do it

6. Write a lambda function to reverse a string.

7. Write a lambda function to check if a string is a palindrome.  do it---slicing

8. Write a lambda function to sort a list of numbers in ascending order.

'''

# 1.
sqr_num = lambda num:num**2
print("Square of number : ",sqr_num(6))

# 2.
even_odd = lambda num : print("Even") if(num%2==0) else print("Odd")
even_odd(18)
even_odd(15)

# 3.
num = lambda n  : n+1   #err
num(10)
print("Sum of num is : ",num)

# 4.
max_num = lambda n1,n2 : print("n1 is max.") if(n1>n2) else print("n2 is max.")
max_num(19,17)

# 5



