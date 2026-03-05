'''
03-03-26--holi
04-03-2026
watch lecture
write a FH program which takes numbers as (12 56) from another file 
and perform addition of it
12+56 = 68

'''
import os

def number_addition(filename):
    if(os.path.exists(filename)):
        with open(filename,"r") as data:
            numbers = data.read()
            print(numbers)
            print(type(numbers))

            split_data = numbers.split()
            print(split_data)

            sum = 0
            for i in split_data:
                sum += int(i)

            print(sum)
    
number_addition("File handling/numbers.txt")

'''
Q. Create a text file containing only digits (e.g., 12345) and write a Python program to read the file and 
calculate the sum of all digits using file handling.

'''

# next shallow and deep copy
