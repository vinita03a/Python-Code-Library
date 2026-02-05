
# Data 23 Jan 2026
# Assignment-1
# Assignement - List_tuple.txt
# Text

# Private comments
# Basic Questions

# 1.Create a list of 5 cities and print the third city using positive indexing and the last city using negative indexing.
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
print(cities[2])   # third city (positive indexing)
print(cities[-1])


# 2.Write a program to create a list of first 10 odd numbers using manual entry.
odd_numbers = [1,3,5,7,9,11,13,15,17,19]
print(odd_numbers)

# 3.Given a list nums = [2, 4, 6, 8, 10], access and print the second-last element using negative indexing.
nums = [2,4,6,8,10]
print(nums[-2]) 
# 4.Concatenate the two lists a = [1,2,3] and b = [4,5,6] and print the result.

a = [1,2,3]
b = [4,5,6]
print(a + b)

# 5.Create a nested list and print a specific element (for example: from [1, [2,3,[4,5]], 6] print 5).
nested = [1, [2,3,[4,5]], 6]
print(nested[1][2][1])

# Slicing & Indexing

# 1.Given colors = ["red","blue","green","yellow","black","white"],

# 	print ["green","yellow"] using positive slicing.
colors = ["red","blue","green","yellow","black","white"]

print(colors[2:4])   # ["green","yellow"]

# 	print ["white","black"] using negative slicing.

print(colors[-1:-3:-1])

# 2.Create a list of first 15 even numbers and use slicing to display only numbers from 8 to 16.
evens = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
print(evens[3:8])

# 3.Write a program to reverse a list using slicing.
print(evens[::-1])

# 4.From the list nums = [100,200,300,400,500,600], extract [300,400,500] using slicing.
nums = [100,200,300,400,500,600]
print(nums[2:5])

# 5.Given x = [1,2,3,4,5,6,7,8,9], print only the odd numbers using step slicing.
x = [1,2,3,4,5,6,7,8,9]
print(x[::2])


# Mutability & Modification

# 1.Create a list marks = [45, 56, 78, 89, 90]. Modify the second element to 60 and the last element to 95.
marks = [45,56,78,89,90]
marks[1] = 60
marks[-1] = 95
print(marks)

# 2.Replace the middle three elements of [10,20,30,40,50] with [25,35,45].
lst = [10,20,30,40,50]
lst[1:4] = [25,35,45]
print(lst)

# List Methods

# 1.Create a list of names and add three new names using append().
names = ["Akanksha","Ravi"]
names.append("Priya")
names.append("Amit")
names.append("Neha")
print(names)

# 2.Create two lists of numbers and merge them using extend().
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)

# 3.Insert "Python" at the 2nd position in the list ["Java","C++","C","Go"].
langs = ["Java","C++","C","Go"]
langs.insert(1,"Python")
print(langs)

# 4.Write a program to delete the element 500 from the list [100,200,300,400,500,600] using remove().
nums = [100,200,300,400,500,600]
nums.remove(500)
print(nums)

# 5.Create a list [10,20,30,40,50], use pop() to delete the last element, and display the modified list.
lst = [10,20,30,40,50]
lst.pop()
print(lst)

# 6.Write a program to sort the list letters = ['d','a','z','c','b'] in ascending order and then in descending order.
letters = ['d','a','z','c','b']
letters.sort()
print(letters)       
letters.sort(reverse=True)
print(letters) 

# 7.Create a list of numbers and display:
numbers = [10,20,30,40,50]

# 	Sum of all elements
print(sum(numbers))
# 	Maximum element
print(max(numbers))
# 	Minimum element
print(min(numbers))

# TUPLE QUESTIONS

# 1. Create a tuple with 5 integers and print its length.
t1 = (1,2,3,4,5)
print(len(t1))

# 2. Create a tuple with 5 strings and print the second last element using negative indexing.
t2 = ("car","bike","phone","mouse","bluetooth")
print(t2[-1])

# 3. From the tuple (10,20,30,40,50), access elements from index 1 to 3 (inclusive of start, exclusive of end).
tuple = (10,20,30,40,50)
print(tuple[1:4])

# 4. Create a tuple ("a", "b", "c") and concatenate it with ("d", "e").
a = ("a", "b", "c") + ("d", "e")
print(a)

# 5. Create a tuple (100,). Print its type and explain why the comma is important.
tup = (100,)
print(type(tup))

# 6. Create a tuple (1,2,3,4,5) and extract the last three elements using slicing.
tuple1 =  (1,2,3,4,5)
print(tuple1[-3:])

# 7. Create a nested tuple (1, (2,3), (4,5,6)) and access 5.
t7 = (1,(2,3),(4,5,6))
print(t7[2][1])

# 8. Swap two variables a=10 and b=20 using tuple unpacking.
a,b = (10,20)
a,b = b,a
print(a,b)

# 9. Create a tuple with duplicate values (5,5,5,10,20) and use count() to find how many times 5 appears.
tup9 = (5,5,5,10,20)
print(tup9.count(5))

# 10. Use the tuple (2,4,6,8,10) and check the index of element 8.
tup10 = (2,4,6,8,10)
print(tup10.index(8))

# 11. Demonstrate tuple packing: assign ("ram", 25, "pune") to a single variable.
person = ("ram",25,"pune")
print(person)

# 12. Demonstrate tuple unpacking: from ("ram", 25, "pune") extract values into 3 different variables.
name,age,city = ("ram",25,"pune")
print(name,age,city)

# 13. Create a tuple (1,2,3,4,5,6,7,8,9,10) and extract every second element using slicing.
t10 = (1,2,3,4,5,6,7,8,9,10)
print(t10[::2])

# Assignement - List_tuple.txt

# Displaying Assignement - List_tuple.txt.t11 = (1,2,3,4,5)
t11 = (1,2,3,4,5)
print(t11[::-1])