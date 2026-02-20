'''
19-02-2026--Holiday

20-02-2026---after lambda funciton

hof - higher order function 
when a function is an argument for another function

inbuilt hof
1. filter
2. map
3. reduce


1. filter() function - it applies function to each element of the sequence 
and gives new object of the elements when condition is True.

Syntax : filter(function,sequence/iterable)    #sequence -(tuple, list etc)

'''

'''
1.  From a list of numbers, filter out only the even numbers.

2.  From a list of numbers, filter out only the odd numbers.  do it

3.  Given a list of words, filter out words whose length is greater than 5.

4.  From a list of integers, filter numbers divisible by 3.

5.  From a list of names, filter names starting with the letter 'A'.

6.  From a list of strings, filter out palindromes.

7.  From a list of ages, filter out ages greater than or equal to 18 (adults).

8.  From a list of numbers, filter prime numbers only.  (user defined)
'''
# 1. 
# numbers = [12,6,13,8,9,3,5,46,16,56]

# def even_odd_check(n):
#     return n%2==0

# even_num = list(filter(even_odd_check,numbers))
# print("list of even numbers = ",even_num)

# # using lambda function

# even_list = list(filter(lambda n : n%2==0,numbers))
# print("List of even numbers : ",even_list)



# # 2.
# numbers = [12,6,13,8,9,3,5,46,16,56]

# def even_odd_check(n):
#     return n%2!=0

# odd_num = list(filter(even_odd_check,numbers))
# print("list of even numbers = ",odd_num)


# # 3
# words = ["python","programming","coding","learning","git","cloud"]

# new_words = list(filter(lambda w : len(w)>5,words))
# print(new_words)



# # 5
# words = ["Arti","Kirti","Akansksha","Ashish","Nitin"]

# new_words_list = tuple(filter(lambda w : w.startswith("A"),words))
# print("List of words start with A : ",new_words_list)

# # 4.

# num_list = list(filter(lambda n : n%3==0,numbers))
# print("List of divisible by 3 numbers : ",num_list)

# # 6

# reverse_string = lambda s : s[::-1]
# str1 = input("enter a string : ")
# print("reversed string is : ",reverse_string)

# # 7. 
# palindrome = lambda s : ("palindrome") if (s==s[::-1]) else ("not palindrome")
# str1 = input("enter a string : ")
# print(palindrome(str1))

# 8



'''
map() function - it applies funciton to each element of a sequence and returns 
transformed elements according to function applied.

Syntax:
map(function,sequence/iterable)
'''

'''
1.  From a list of numbers, create a new list with each number squared.

2.  Given a list of words, convert them all to uppercase. do it.

3.  From a list of numbers, create a new list with each number doubled. do it.

4.  From a list of numbers, return a list containing "Even" or "Odd" for each number.

5.  Given a list of strings, return their lengths.

'''

# 1.
lst = [2,3,4,5,6,7,8]

sqr_list = list(map(lambda num : num**2 , lst))
print("list of squared elements : ",sqr_list)

numbers = [8,9,5,16,17,71,91,44]

even_odd = list(map(lambda num : "even" if(num%2==0) else "odd", numbers))
print(even_odd)

# 2.
words = ["today","friday","date"]
lst = list(map(lambda word1 : word1.upper(),words))
print(lst)

# 3.
lst = [2,3,4,5,6,7,8]

sqr_list =  list(map(lambda num : num*num , lst))
print("list of double number : ",sqr_list)

# 4.
numbers = [1,2,3,4,5]

even_odd = list(list(map(lambda num : "even" if(num%2==0) else "odd")))
print(even_odd)


# 5
words = ["apple","banana","mango","grapes"]
lengths = list(map(lambda w : len(w),words))
print(lengths)

'''
reduce() funciton - it applies function to pair of elements and returns 
a cumulative(single) value as output
like your aggregate function, sum of elements, max/min elements in list/sequence


syntax :
reduce(function,sequence)

from functools import reduce

'''
from functools import reduce

# sum of elements in list 
numbers = [12,6,13,8,9,3,5,46,16,56]

sum_elements = reduce(lambda n1,n2 : n1+n2 , numbers)
print(sum_elements)

# max number form list
numbers = [12,6,13,8,9,3,5,46,16,56]

max_elements = reduce(lambda x,y : x if x > y else y, numbers)
print(max_elements)

# min number from list
numbers = [12,6,13,8,9,3,5,46,16,56]

min_elements = reduce(lambda x,y : x if x < y else y, numbers)
print(min_elements)

'''
FILTER() QUESTIONS

 

1. Filter numbers divisible by 3 from a list.

2. Filter words that contain letter 'e'.

3. Filter students whose marks are above 75 from a list.

4. Filter words whose length is more than 4.

5. Filter negative numbers from a list.

MAP() QUESTIONS

1. Convert temperatures from Celsius list to Fahrenheit.

2. Multiply each number in list by 5.

3. Convert list of strings into their lengths.

4. Convert list of strings into integers.

5. Find length of each word in a list.

REDUCE() QUESTIONS

1. Find the factorial of a number using reduce().

2. Find the largest string in list based on length.

3. Find total sum of squares of numbers.

4. Find minimum number from list.

5. Concatenate all strings in a list into one string.

'''
# 1 . Filter numbers divisible by 3 from a list.

num_list = list(filter(lambda n : n%3==0,numbers))
print("List of divisible by 3 numbers : ",num_list)

# 2.  Given a list of words, convert them all to uppercase. do it.

words = ["cse","ds","AI","se","da"]
w = list(filter(lambda w1 : 'e' in w1, words))
print(w)

# 3
marks = [65,82,50,85,75,46,66]
result = list(filter (lambda lst : lst>75, marks))
print(result)

# 4
words = ["hi","hello","python","ok","world"]
result = list(filter(lambda w : len(w) > 4,words))
print(result)

# 5
numbers = [10,-5,3,-2,-8,6]
result = list(filter(lambda x : x < 0 , numbers))
print(result)

