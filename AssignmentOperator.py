
# Docstring for Test&Assignment.AssignmentOpertor

# 1. Arithmetic Operators
# -----------------------
# 1. Write a program to add two numbers entered by the user.

num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
optr = input("Enter a operatot : ")
print("Two number sum is : ",num1+num2)


# 2. Find the remainder when 29 is divided by 5.
n1 = 29
n2 = 5
#modulus (%) - remainder
print("Modulus - ",n1%n2)
# 3. Calculate the square of a number using the ** operator.
a=4
print("Exponential - ",a**4)

# 4. Use floor division (//) to divide 17 by 4.
n1 = 17
n2 = 4
print("Floor division -",n1//n2)

# 5. Multiply two numbers and print the result.

n1 = 16
n2 = 5
print("Product -",n1*n2)


# 2. Relational (Comparison) Operators
# ------------------------------------
# 1. Check if two given numbers are equal or not.
a = 56 
b = 72
print(a!=b)
# 2. Write a program to check if 45 is greater than 20.


# 3. Compare two strings "apple" and "banana" using <.
# 4. Check if a number is less than or equal to 100.
# 5. Test if 10 != 15 and display the result.

# 3. Logical Operators
# --------------------
# 1. Check if a number is between 10 and 50 using and.
# 2. Write a program to check if a number is either less than 0 or greater than 100 using or.
# 3. Use not to invert the result of a boolean expression.
# 4. Evaluate: (5 > 3) and (10 < 20).
# 5. Evaluate: (7 == 7) or (8 < 5).

# 4. Assignment Operators
# -----------------------
# 1. Assign the value 25 to a variable and print it.
# 2. Use += to add 10 to a variable.
# 3. Subtract 5 from a variable using -=.
# 4. Multiply a variable by 3 using *=.
# 5. Divide a variable by 2 using /= and print the result.

# 5. Bitwise Operators
# --------------------
# 1. Find the result of 6 & 3.
# 2. Find the result of 6 | 3.
# 3. Find the result of 6 ^ 3.
# 4. Perform left shift on 5 by 2 bits (5 << 2).
# 5. Perform right shift on 16 by 3 bits (16 >> 3).

# 6. Identity Operators
# ---------------------
# 1. Check if two lists [1,2,3] and [1,2,3] are the same object using is.
# 2. Compare two variables referring to the same list with is.
# 3. Check if two tuples (1,2) and (1,2) are not the same object.
# 4. Create two variables pointing to the same string and check with is.
# 5. Verify if a copied list is different from the original list using is not.

# 7. Membership Operators
# -----------------------
# 1. Check if the number 5 exists in the list [1,2,3,4,5].
# 2. Verify if "a" is in the string "apple".
# 3. Check if "dog" is not in the list ["cat", "cow", "goat"].
# 4. Write a program to see if 10 is in the tuple (15,18,10,89).
# 5. Check if "Python" is not in the list ["Java", "C++", "Ruby"].

# 8. Combination of operators.
# ---------------------------
# 1. For x = 20, y = 10, print (x - y == 10) and (x / y == 2).

# 2. For a = 18, b = 9, print (a // b == 2) and (a % b == 0).

# 3. For m = 7, n = 3, print (m * n == 21) or (m + n == 12).

# 4. For p = 16, q = 4, print (p / q == 4) and (p ** q == 256).

# 5. For x = 25, y = 5, print (x % y == 0) and not (x < y).

# 6. For a = 11, b = 2, print (a // b == 5) and (a % b == 1).

# 7. For p = 7, q = 14, print (p * 2 == q) and (q % p == 0).

# 8. For a = 12, b = 6, print (a / b == 2) and (a % b == 0).

# 9. For x = 9, y = 3, print (x > y) and (x % y == 0).

# 10. For m = 5, n = 25, print (n / m == 5) or (m * m == n).

# 11. For p = 8, q = 2, print (p ** q == 64) and (p / q == 4).

# 12. For a = 15, b = 4, print (a // b == 3) and not (a % b == 0).

# For example ,do like below.
# # For p = 7, q = 14, print (p * 2 == q) and (q % p == 0)

# p = 7
# q = 14
# print(p * 2 == q)  # 7 * 2 == 14 = T
# print(q % p == 0)  # 14 % 7 == 0 = T
# print("Q - ",(p * 2 == q) and (q % p == 0))   # T and T = T

# 9. Membership + Logical
# -----------------------

# 1. For s = "developer", print 'd' in s.

# 2. For s = "programming", print 'x' not in s.

# 3. For lst = [2, 4, 6, 8, 10], print 6 in lst.

# 4. For lst = [100, 200, 300], print 150 not in lst.

# 5. For d = {"x": 10, "y": 20}, print 'z' not in d.

# 6. For s = "datastructure", print "struct" in s.

# 7. For s = "computerscience", print ("science" in s and "math" not in s).

# 8. For s = "informationtechnology", print ("tech" in s and "IT" not in s).

# 9. For s = "machinevision", take "vision" from user and check if it is in s.

# 10. For s = "natural language processing", print ("language" in s and "speech" not in s).

# Tuple Packing and Unpacking Questions.

# 1. Pack 3 numbers (10, 20, 30) into a tuple and unpack them into variables a, b, c. Print each variable.

# 2. Pack values "apple", "banana", "cherry", "mango" into a tuple and use extended unpacking to assign the first value to x, the last value to y, and the middle values to a list named rest. Print x, rest, y.

# 3. Given a tuple (5, 10, 15, 20, 25), unpack the first two values into variables a, b and the remaining values into a list using *. Print all.

# 4. Take a tuple (100, 200, 300, 400) and unpack it into variables w, x, y, z. Then print the sum of all unpacked variables.

# 5. Given tuple ("Python", "Java", "C", "C++", "Go"), use extended unpacking to store the first element in lang1, the last element in lang2, and the rest in others. Print lang1, lang2, and others.

