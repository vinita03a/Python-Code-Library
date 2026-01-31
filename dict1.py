'''
Docstring for dict1

dictionary - its collection of elementsin key:value pair enclosed in {,}
'''

d = {"batch1":"pyhton", "batch2":"java","batch3":"AI" }
print(d)
print(len(d))

details = {
    "name" : "Vinita Awhad",
    "age" : 24,
    "contact":74709968254,
    "location":"Pune"
}

print(details)

# duplicacy 

#  keys as duplicate not allowed
details = {
    "name" : "Vinita Awhad",
    "name" : "Vini",
    "age" : 24,
    "contact":74709968254,
    "location":"Pune"
}

print(details)

# duplicate values allowed
details = {
    "name" : "Vinita Awhad",
    "age" : 24,
    "contact":74709968254,
    "location":"Pune",
    "new_location":"Pune"
}

print(details)

# accessing values using key

emp_details = {
    "emp_name" : "Nisha",
    "emp_id" : "IBM123",
    "emp_location":"Mumbai"
}
print("employees details :\n", emp_details)
print(emp_details["emp_name"])
print(emp_details["emp_location"])

# cannot do slicing

'''
Task:
     
d1 = {"emp_name":"Akshay" , "age":34 , "salary" : 67000 . "emp_ID":1278 , "location":"pune"}
access salary data
access location data
'''


d1 = {
    "emp_name":"Akshay" , 
     "age":34 , "salary" : 67000 ,
     "emp_ID":1278 , "location":"pune"
        }
print(d1 ["salary"])
print(d1["location"])



# mutability

student_details = {
    "s_name" : "Pranali",
    "s_rollNum":172,
    "s_college":"COEP"
}

student_details["s_rollNum"]=173
print("updated data : ",student_details)
student_details["s_college"] = "Wadia"
print("upadated details : ",student_details)

# can add new key:value pair
student_details["s_location"] = "Pune"
print("Updated new detail : ",student_details)


# list as a value in dictionary

data = {
    "name": ["priya","nisha","dev","ved","kartik"],
    "marks":[56,78,91,37,81],
    "college":"Wadia",
    "location":"Pune"
}

# access "ved"
print(data["name"][3])

# access 91
print(data["marks"][2])

# nested dictionary

data1 = {
    "ML" : {1:"batch1",2:"batch3"},
    "AL" : {"batch1":"python","batch2":{1:"python",2:"mysql"},"batch3":"powerBI"},
    "DS": "Machine learning"
}

print(data1["ML"][2])
print(data1["AL"]["batch2"][2])

print("--------Methods---------")

# .get() - it returns value for key specified.

student_details = {
    "s_name" : "Pranali",
    "s_rollNum":172,
    "s_college":"COEP"
}

print(student_details.get("s_rollNum"))

# .keys() - it returns list of keys.

print(student_details.keys())

# .values() - it returns list of values.

print(student_details.values())

# .items() - it returns list of key:value pairs.
print(student_details.items())


# pop() - it deletes a value

student_details.pop("s_name")
print(student_details)

# .popitems() - it deletes last key:value pairs
student_details = {
    "s_name" : "Pranali",
    "s_rollNum" : 172,
    "s_college":"COEP"
}

student_details.popitem()
print(student_details)