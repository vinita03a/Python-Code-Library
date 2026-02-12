# 02-02-2026---after alphabeticalpattern.py

'''
Docstring for Comprehension.comprehension

comprehension - it is compact way of iterating over a sequence in single line of expression.
list comprehension - [expression for i in range() if(condition)]
set comprehension - {expression for i in range() if(condition)}
dictionary comprehension - {key_expre. : value_expre. for i in range() if(condition)}
generator expression - (expression for i in range() if(condition))

'''

even_num = []
for i in range(1,21):
    if(i%2==0):
        even_num.append(i)

print("Even list - ",even_num)

print("------------list compre----------------")

even_num = [i for i in range(1,21) if(i%2==0)]
print(even_num)

num_range = [num for num in range(12,19)]
print(num_range)

rev_num = [n for n in range(10,0,-1)]
print(rev_num)

'''

1. create list of marks greater than 50 from given list
2. to generate list of squares from 1-10
3. Create a list of words from a sentence "List comprehensions are powerful" that have length greater than 4.
4. Use list comprehension to create a list of tuples (number, square) for numbers 1 to 5.
5. Create a list comprehension to convert all strings in a list to uppercase.

'''

# 1

marks = [20,56,17,82,91,45,76,44]

new_marks_list = [m for m in marks if(m>50)]
print("List of marks>50 : ",new_marks_list)

# 2

sqr_list = [n**2 for n in range(1,11)]
print("list of sqr of numbers : ",sqr_list)

# 3

str_list = "List comprehensions are powerful"
list = [n for n in str_list.split() if len(n)>4]

print(list)


# 4


# 5

s = ["red","blue","green"]
uppercase = [ word.upper() for word in s]
print(uppercase)

print()
print("--------------set comprehension--------------------")

'''
1. Write a set comprehension to label numbers as even or odd.
2. Create a set comprehension to generate squares of numbers from 1 to 15, excluding multiples of 5.
3. Create a set comprehension to find unique vowels in a given sentence.

'''

# 1

data = {29,56,17,19,27,54,44,1}

labeled_num = {str(n)+"-even" if(n%2==0) else str(n)+"-odd" for n in data}
print(labeled_num)


# 2

sqr_numbers = {n**2 for n in range(1,16) if(n%5!=0)}
print(sqr_numbers)

# 3
s = input("Enter a string : ")
vowel = "aeiouAEIOU"
w = {ch for ch in s if(ch in vowel)}
print(w)


print()
print("-----------dict comprehsion--------------")

'''
1. Write a dict comprehension to create a dictionary of numbers and their squares from 0-4.
2. Write a dict comprehension to filter only even values from a dictionary. 
    d={'a':1,'b':2,'c':3,'d':4}
3. Use dictionary comprehension to swap keys and values in a given dictionary.
    d = {'a': 1, 'b': 2, 'c': 3}

'''

# 1

d1 = {n:n**2 for n in range(0,5)}
print(d1)

# 2
d={'a':1,'b':2,'c':3,'d':4}

d2 = {k:v for k,v in d.items() if(v%2==0)}
print(d2)

# swapping
# a = 56
# b = 78

# a,b = b,a
# print(a,b)

# 3
d = {'a': 1, 'b': 2, 'c': 3}
d3 = {v:k for k,v in d.items()}
print(d3)

'''
generator expression - it is a lazy execution ,  it generates single element at a tiem instead of storing whole sequence in single memory location

'''

# display tuple of cubes of number.

# tup_cubes = (n**3 for n in range(2,11))
# print(tuple(tup_cubes))

# display list of cubes of number

# list_cubes = (n**3 for n in range(2,11))
# print(list(list_cubes))


print("=================Questions===================")


'''

List comprehension
1. Write a list comprehension to create a list of numbers from 1 to 10.
 
2. Write a list comprehension to create a list of even numbers between 1 and 20.
 
3. Write a list comprehension to create a list of squares of numbers from 1 to 10.
 
4. Write a list comprehension to create a list of cubes of numbers from 1 to 5.
 
5. Write a list comprehension to create a list of all characters in the string "Python".
 
6. Write a list comprehension to create a list of vowels from the string "education".
 
7. Write a list comprehension to create a list of numbers between 1 and 30 that are divisible by 3.

8. Write a list comprehension to create a list of the first letters of each word in ["apple", "banana", "cherry"].
 
9. Write a list comprehension to create a list of numbers from 1 to 10, but store "Even" for even numbers and "Odd" for odd numbers.
 
10. Write a list comprehension to create a list of squares for only even numbers between 1 and 20.
'''

# 1
number = [n for n in range(1,11)]
print(number)

# 2
even_num = [i for i in range(1,21) if(i%2==0)]
print(even_num)

# 3
number = [n**2 for n in range(1,11)]
print(number)

# 4
number = [n**3 for n in range(1,5)]
print(number)

# 5
s = "Python"
w = [ch for ch in s]
print(w)

# 6
s="education"
vowel = "aeiouAEIOU"
w = {ch for ch in s if(ch in vowel)}
print(w)

# 7
num = [n for n in range(1,31) if(n%3==0)]
print(num)

# 8
v=["apple", "banana", "cherry"]
sen = [ch[0] for ch in v]
print(sen)

# 9 
num = [str(n)+"-Even" if n%2==0 else str(n)+"-Odd" for n in range(1,11)]
print(num)


# 10
sqr = [n**2 for n in range(1,21) if n%2==0]
print(sqr)

'''
13. Create a dictionary mapping numbers to their squares (1 to 10).
14. Reverse keys and values of a dictionary using comprehension.
15. Create a dictionary from two lists: one list of keys and another list of values.
16. Filter a dictionary to keep only items where value is even.
17. Convert a list of tuples into a dictionary using comprehension.
18. Given a word, count frequency of each character using dictionary comprehension.
19. Map each word in a sentence to its length.
20. Create a dictionary of items and their prices with discount applied using comprehension.
'''