'''

=== 10 Theory Questions ===
1. Define mutable and immutable data types with examples.
2. What is the difference between list and tuple?
3. Explain indexing and slicing in Python with an example.
4. What is the difference between append() and extend() in lists?
5. Define a dictionary. How is it different from a set?
6. What is the difference between isalpha(), isdigit(), and isalnum()?
7. What is string immutability? Explain with an example.
8. Define packing and unpacking in tuples.
9. What is the difference between sequential and mapping datatypes?
10. Write two differences between set and frozenset.


=== 10 Code Correction Snippets ===
1.
lst = [10,20,30]
print(lst[3])    # IndexError

2.
tup = (10,20,30)
tup[1] = 50
print(tup)

3.
colors = ["red","blue","green"]
colors.insert(5,"yellow")
print(colors)

4.
name = "Python"
print(name.lowercase())

5.
num = [2,4,6,8,10]
print(num[::-0])   # Error in slicing

6.
data = {"a":10,"b":20}
print(data[2])     # Wrong key access

7.
fruits = "apple,banana,orange"
fruit_list = fruits.split(" ")
print(fruit_list)

8.
sentence = 'It's raining'
print(sentence)

9.
days = ["Mon","Tue","Wed"]
days.remove("Sunday")
print(days)

10.
marks = (78,45,90)
print(marks.index(100))   # ValueError


=== 10 Program Questions ===
1. Create a list of 10 odd numbers and print it.
2. Create a list of 10 even numbers and print their sum.
3. Create a nested list of your choice and access inner elements.
4. Take a string input and check if it is a palindrome.
5. Take a string and print it in reverse using slicing.
6. Take a list of numbers and print only the even numbers.
7. Take two lists and concatenate them.
8. Create a dictionary of 5 students with their marks and print the keys.
9. Create a tuple and demonstrate packing and unpacking.
10. Create a set of colors, add a new color, and remove one color.

'''