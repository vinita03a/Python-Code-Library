# 03-02-2026

'''
Docstring for Conditionals.ifelse

if else

Syntax :
if(condition):
#    block of code
else 
     #block of code

'''
# indentation-

x = 67
if(x>50):
    print("is greater.")
else:
    print("is not greater.")

# age criteria

age= int(input("Enter the age to check eligibility : "))
if(age>=18):
    print("can vote.")
else:
    print("cannot vote.")


'''
1.  Check if a number is even or odd.
2. Check if a number is positive or negative.
3. Check if a given string is empty or not.
4. Check if a number is divisible by 5.
5. Check if the first character of a string is vowel or consonants.
6. Check if a number is divisible by 2 but not by 4.
'''

# 1.  1.  Check if a number is even or odd.
n = int(input("Enter a number to check even/odd :"))
if(n%2==0):
    print(f"{n} is even number.")
else:
    print(f"{n} is odd number.")


#2 Check if a number is positive or negative.
n = int(input("Enter the number : "))
if(n>0):
    print("is positive number")
else:
    print("is negative number")

# 3 Check if a given string is empty or not.

string = input("Enter a string : ")
if(string == ""):
    print("String is empty.") 
else:
    print("String is not empty.")

# 4 Check if a number is divisible by 5.

n= int(input("Enter a number : "))
if(n%5==0):
    print("divisible by 5.")
else:
    print("not divisible by 5.")

# 5. Check if the first character of a string is vowel or consonants.

s = input("Enter a string : ")
vowel = "aeiouAEIOU"
if(s[0] in vowel):
    print("first character is vowel.")
else:
    print("first character is not vowel.")


# 6.  Check if a number is divisible by 2 but not by 4.

