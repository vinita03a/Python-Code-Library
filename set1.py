'''
Docstring for set1

set - it is an unordered collection of data {,}
onlyk unique elements allowes
'''

set1 = {10,78,92,67,99}
print(set1)
print(len(set1))

#duplicacy
set2 = {"pyhton", "java", "c++","python", "java", "html"}
print(set2)


set3 = {True,False,0,1,1,45,78}
print(set3)

# accessing elements
# colors = {"red","green","yellow","blue"}
# print(color[2])

'''print(color[2])
          ^^^^^
          TypeError: 'set'is not subscripated or
          NameError: name 'color' is not defined. Did you mean: 'colors'?

'''

# mutability -immutable
# colors = {"red","green","yellow","blue"}
# colors[1]="maroon"
# print(colors)


'''
 colors[1]="maroon"
    ~~~~~~^^^
TypeError: 'set' object does not support item assignment
'''

# methods of set
#  .add() , .update()

city = {"pune","mumbai","nanded"}
city.add("nashik")
print(city)

city = {"pune","jalna","mumbai"}
more_cities = {"patna","nashik"}
city.update(more_cities)
print(city)

# pop() , remove() , discard()

data = {"pyhton","java","aws","ML","DS","DA"}
data.pop()
print(data)

data = {"pyhton","java","aws","ML","DS","DA"}
data.remove("DS")
print(data)

data = {"pyhton","java","aws","ML","DS","DA"}
data.discard("python")
print(data)


# difference of discard and remove.

# issubset() - it checks if all elements of one set is present is another set
# issuperset() - it checks if the set contents are present in another set.
# isdisjoint() - it checks if both sets are not common.

# issubset()
set1 = {2,4,6}
set2 = {8,9,10,6,2,11,4,18}

print(set1.issubset(set2))
print(set2.issubset(set1))

#  issuperset()
set1 = {2,4,6}
set2 = {8,9,10,6,2,11,4,18}

print(set2.issuperset(set1))
print(set1.issuperset(set2))

# isdisjoint()

set1 = {2,4,6}
set2 = {1,3,5}

print(set1.isdisjoint(set2))

'''
union - set of unique elements when combining two sets
.union() , | pip operator
and 
intersection - set of common elements when combining two sets
.intersection() , & operator
'''

# union

set1 = {9,8,5,1,10}
set2 = {1,12,7,8,19,13}

set3 = set1.intersection(set2)
print("using union method",set3)
set4 = set2|set1
print("using | pip operator",set4)

#intersection

set1 = {9,8,5,1,10}
set2 = {1,12,7,8,19,13}

set5 = set1.intersection(set2)
print(set5)
set6 = set2&set1
print(set6)

# difference - removing set2 elements from set1
# .difference() , -minus  operator

set1 = {9,8,5,1,10}
set2 = {1,12,7,8,19,13}

set7 = set1.difference(set2)
print(set7)

set8 = set2-set1
print(set8)
