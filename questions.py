# 02-02-2026

# TASK:


# LIST
# 1.Create a list from user input and print the first and last element using indexing.
# 2.Take a list of string numbers from the user and print a sublist of the first 3 elements using slicing.
# 3.From a user-created list, print the list in reverse order using slicing.
# 5.Input a list of items from the user and use the + operator to concatenate it with another list (e.g., [100, 200]).
# Let L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
# 7.Using a negative step, produce a list that starts at the last element and takes every 2nd element moving leftward.
# Expected o/p - [9, 7, 5, 3, 1]


# 1 user list using split() method
# courses = input("Enter courses :").split()
# print(courses)
# print(type(courses))

# 1.Create a list from user input and print the first and last element using indexing.

name = input("Enter names : ").split()
print(name)
print("first element : ",name[0])
print("last element : ",name[-1])


# 2
number = input("Enter the string number : ").split()
# sub_list = input("Enter sublist").split()
print(number[:3])

# 3
number = input("Enter the number : ").split()
print(number[::-1])

# 4
number = input("enter the list").split()
print(number+[100,200])

# 5
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[::-2])

'''LIST
1. Given a list of numbers, use slicing to create a new list containing only the middle elements (exclude first and last elements).
2. Write a program to reverse a list using slicing.
3. Given lst = [10, 20, 30, 40, 50, 60], use slicing to create:
   a) a list of first three elements
   b) a list of last three elements
4. Given two lists, use list concatenation to create a new list that contains elements of both lists.
5. Write a program to add multiple elements to an existing list using a list method.
6. Given a list, use a list method to remove a specific element from the list.

'''


list = input("Enter the elements :").split()
print(list)







