#length - len() - number of elements

courses= ["python","java","ds","da","ml","ai","aws","digital marketing"]
print("Length - ",len(courses))


#relation between length and index

#index = length-1
# 7 = 8-1

print(courses[-1])
print(courses[len(courses)-1])

#concatenation









# Mutable datatype-



names = ["nisha","priya","Kartik","Disha"]
names[3]="Kirti"
print(names)

names[1:3]=["neha","dev"]
print(names)

# nested list

nested_list = [23,45,[56,78,99],[1,2],90,27]
print(nested_list[2][2])
print(nested_list[3][1])



marks = [89,56,27,18,45,81]
marks.sort(reverse=True)
print((marks))