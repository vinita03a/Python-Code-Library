# 30-January-2026

'''
Docstring for Datas.py.string1

string - its collection of characters enclosed in '', "", """ """
'''


word = "Hello"
print(word)
print(len(word))


word1 = 'Codenera'
print(word1)
print(len(word1))

para = """
  2-Interepreted Language:
  executes code line by line

  3-High level  prograning language
  low level details can be abstracted and developer can focus on the required functionality

  4- Dyanamically type:
  Statically typed(c,c++,java) / Dynamically typed(python),
  no need to define the type of data

"""
print(para)

word2 = "Hello World"
print(word2)
print(len(word2))


#accessing elements
greet = "Hello world"
print(greet[1])
print(greet[4:9])

# backslash (escape character)
# "\". \',\n , \t


sentence = "I am \"AkanKsha\""
print(sentence)


sen1 = 'It\'s raining'
print(sen1)
print(len(sen1))


# \n - newline character , \t - tab space
fruits = "apple\nbanana\nchickoo"
print(fruits)
print("Menu:\n1.Biryani.\n2.Pizza.")
heading = "Name\tCity"
data = "Kriti\tPune"
print(heading)
print(data)
# concatination - joining of strings
first_name = "Akanksha"
last_name = "Ramane"
full_name = first_name+" "+last_name
print(full_name)


#case conversion
#  .lower(), upper() , capitalize()
name = "kirti"
upper_case = name.upper()
print(upper_case)

name = "KIRTI"
lower_case = name.lower()
print(lower_case)

name = "kirit"
capital = name.capitalize()
print(capital)

# content checking
# .isalpha() , .isdigit() ,.isalnum()

s = "abc"
print(s.isalpha())
s = "abc12"
print(s)

s1 = "234"
print(s1.isdigit())
s1 = "234abc"
print(s1.isdigit())

s2 = "abc123"
print(s2.isalnum())
s2 = "123"
print(s2.isalnum())


#split() - it return list of substrings, according to separator provided.
# bydefault separator is space

s = "Hello I live in Pune"
words = s.split()
print(words)

fruits = "apple,banana,cherry"
fruit_list = fruits.split(sep=",")
print(fruit_list)

data = "2026/30/01"
date = data.split(sep="/")
print(date)



# join() - it takes all substring in an iterable(list,tuple etc.)
# and joins all together in a string, acc. to separator provided.
# syntax : "".join(iterable)
fruits = ["apple","cherry","banana","jackfruit"]
fruit_join = "-".join(fruits)
print(fruit_join)
print(type(fruit_join))    # <class 'str'>
data = ("2026","30","01")
date = "/".join(data)
print(date)
name = "akanksha"
asc_order = "".join(sorted(name))
print(asc_order)
# do for descending order.


# strip() - removes leading and trailing white spaces of string

word = "    Hello World "
word_strip = word.strip()
print(word_strip)

word1 = "$$Codenera$$"
new_word = word1.strip("$$")
print(new_word)

# replace() - replace old string with new string

name = "@k@nsksh@"
replace_word = name.replace("@","a")
print(replace_word)

# find() , startswith(), endswith(), count()



#----- 31-January-2026---------

# 1. s = "apple banana mango grapes"
# Split the string into a list of words.
# 2. s = "red,green,blue,yellow"
# Split using comma (,) as separator.
# 3. s = "Python@@Java@@C@@C++"
# Split using @@.

# 4. s = "name=Akanksha;course=Python;year=2025"
# Split using ; and display list.

# 5. words = ["apple", "banana", "mango"]
# Join them with , .


#1.
s ="apple banana mango grapes"
fruits = s.split()
print(fruits)

#3
s = "Python@@Java@@C@@C++"
courses = s.split()
print(courses)


#4
s = "name=Akanksha;course=Python;year=2025"
student = s.split(sep=";")
print(student)


#5

words = ["apple", "banana", "mango"]
fruits = ",".join(words)
print(fruits)
