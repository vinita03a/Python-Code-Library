# 29-01-2026
'''
Docstring for Datas.py.tuple1

tuple - it is ordered collection of data enclosed in (,)
features:
ordered
'''

t1 = (23,45,67)
print(t1)
print(len(t1))

signals = ("red","yellow","green")
print(signals)

# duplicacy
numbers = (23,56,23,45)
print(numbers)

t1 = (23,45,67)
print(t1)
print(type(t1))


t2 = (23,45,67)
print(t2)
print(type(t2))   #<class 'tuple'

l1 = [7]
print(l1)
print(type(l1))

# accessing element using index
signals = ("red","yellow","green")
print(signals[1])

print(signals[1:])

#concatenation
tup1 = (10,20)
tup2 =(30,40)
concat = tup1+tup2
print(concat)

'''
directon = ("east","west","north","south")
direction[-1]="south"
TypeError : 'tuple' object does not support item assignment
'''
 

# 30-01-2026
'''
methods in tuple
count(), index()

'''

# count() - count

data = (34,23,24,56,6,34,78,34,10,19)
cnt = data.count(34)
print(cnt)

# index() - it returns index value of first occured element
data = (23,24,34,23,24,56,6,8,9,11,34,78,12,91,34,10,19)
idx = data.index(34)
print(idx)

idx1 = data.index(34,5)
print(idx1)

'''
packing-assigning multiple values to single tuple variable
unpacking - extracting those values
'''

data = ("banana","yellow",3,"kerala")   #packing
fruit,color,days_old,area=data #unpacking

print(fruit)
print(color)
print(days_old)
print(area)

data1 = ("banana","mango","yellow",3,"kerala")
*fruit,color,days_old,area = data1
print(fruit)
print(color)


data2 = (1,2,3,4,5,6,7,8,9,10)
f_num,s_num,*rem_num,last_num = data2
print(f_num)
print(s_num)
print(rem_num)
print(last_num)


'''
info = ("disha",25,45,26,17,"pune","maharashtra")
    o/p
    Name = disha
    Age = [25,45,26,27]
    City = pune
    State = maharashtra
'''
info = ("disha",25,45,26,27,"pune","maharashtra")
Name,*Age,City,State = info
print("Name = " , Name)
print("Age  = " , Age)
print("City = " , City)
print("State = ", State)

