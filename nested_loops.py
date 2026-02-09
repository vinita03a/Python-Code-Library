# after pass statment - 09-02-2026
'''
Docstring for Looping.nested_loops

nested loop - loop inside another loop


1. Given a list of lists, print all elements using nested for loops.
2. Given a list [1, 2, 3], print all possible pairs (a, b) using nested for loops.
3. Given a string "abc", print all possible pairs of characters.
4. Given two lists, print all pairs (a, b) where a is from the first list and b is from the second list.
5. Given a list [1, 2, 3, 4], print all pairs (a, b) where both numbers are even.

'''

# 1.

list1 =[[10,20] , [30,40] , [50,60]]
# [10,20,30,40,50,60]   -> flattening of list

for i in list1:
    for j in i:
        print(j)
print()

# 2
lst = [1,2,3]
# (a,b)

for a in lst:   #1
    for b in lst:      # 1 2 3
        print((a,b))
print()

# isinstance() function - it is basically used for type checking , like type(x)
# flattening of list

# lst = [[20,34],8 ,91,[56,10]]
# flattened_list = []
# for i in lst:
#     if(  isinstance(i,list) ):
#         for j in i:
#             flattened_list.append(j)
#     else:
#         flattened_list.append(i)

list2 = [10,30,[20,78],(20,89,15),16,81]
flattened_list =[]
for i in lst:
    if(  isinstance(i,list2) ):
        for j in i:
            flattened_list.append(j)
    else:
        flattened_list.append(i)






