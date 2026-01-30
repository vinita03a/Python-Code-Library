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

