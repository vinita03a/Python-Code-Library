# 02-feb-2026---9am to 1pm

'''
Docstring for Datas.py.type_casting


type casting/coversion - converting one type of data 
implicit type casting
explicit type casting


'''
# implicit
a = 3.14
print("Type : ",type(a))

# explicit

# to convert int to float and str

x = 45
print(f"{x}, type-{type(x)}")

x_float = float(x)
print(f"{x_float}, type-{type(x_float)}")

x_str = str(x)
print(f"{x_str} , type-{type(x_str)}")

# to convert flaot to int and str - do it

# to convert str to float and int

contact = "854636874"
print(f"{contact}, type-{type(contact)}")

contact_int = int(contact)
print(f"{contact_int} , type - {type(contact_int)}")

pi = "3.14"
pi_float = float(pi)
print(f"{pi_float} , type - type(pi_float)")

num1 = "56"
num2 = "12"
add = int(num1)+int(num2)
print(add)


# list() , tuple() , str() , set() , dict()

marks = [23,45,67,89,91,54,67]
print(marks)

tuple_convert = tuple(marks)
print(tuple_convert)

set_convert = set(marks)
print(set_convert)

# tuple converting

data = ("red", "graen","yellow")

list_convert = list(data)
print(list_convert)
list_convert[1]="green"
print(list_convert)

new_data = tuple(list_convert)
print("Updated tuple value : ",new_data)

# convert to set

# convert set to list and tuple - do it

courses = []
print(courses)
print(type(courses))

courses.append("python")
courses.append("java")
courses.append("aws")
print(courses)

tup = ()
print(tup)
print(type(tup))
new_tup = tup + (1,2,3,4)
print(new_tup)

# do for str
# s = ""

d = {}
print(d)
print(type(d))

d["emp_name"] = "Kartik"
d["emp_id"] = "IBM234"
print(d)









