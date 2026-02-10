# 09-02-2026 after nested_loops.py
'''
Docstring for Looping.Patterns.starpattern


1. Square Pattern
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
2. Right-angled Triangle
*
* *
* * *
* * * *
* * * * *
3. nverted Right-angled Triangle
* * * * *
* * * *
* * *
* *
*
4. Pyramid
    *
   * *
  * * *
 * * * *
* * * * *
5. Inverted Pyramid
* * * * *
 * * * *
  * * *
   * *
    *
    
6. Right-aligned triangle
        *
      * *
    * * *
  * * * *
* * * * *
7. Inverted right-aligned triangle
* * * * * 
  * * * *
    * * *
      * *
        *
        
8. diamond pattern
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''


'''
1. Square Pattern
           1 2 3 4 5

1          * * * * *
2          * * * * *
3          * * * * *
4          * * * * *
5          * * * * *


'''

r = 5
for i in range(1,r+1):     #(1,6)
    print("* "*r)
print()

# 2. Right-angled Triangle
# *
# * *
# * * *
# * * * *

r = 5
for i in range(1,r+1):
    print("* "*i)
print()

# 3. Inverted Right-angled Triangle
# * * * * *
# * * * *
# * * *
# * *
# *


r=5
for i in range(r,0,-1):     #(5,0)
    print("* "*i)


# 4. Pyramid
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# r = 5
# for i in range(1,r+1):     #(1,6)
#     print(" "*(r-i) + "* "*i)

'''
dry run
 
when i = 1
" "*(4) + "* "*1
     *
when i = 2
" "*(3) + "* "*2
    * *
and so on

'''

# 5. Inverted Pyramid
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

r=5
for j in range(r-1,0,-1):               #(4,0)
        print(" "*(r-j) + "* "*j)



print()

# -------------10-02-2026---------------

# 6. Right-aligned triangle
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

r = 5
for i in range(1,r+1):
    print("  "*(r-i) + "* "*i)
print()


# 7. Inverted right-aligned triangle
# * * * * * 
#   * * * *
#     * * *
#       * *
#         *

r = 5
for i in range(r,0,-1):
    print("  "*(r-i) + "* "*i)
print()


# 8. diamond pattern
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# '''

r = 5

# upper part
for i in range(1,r+1):                 # (1,6)
    print(" "*(r-i) + "* "*i)

# lower part(r-1,0,-1)
for j in range(r-1,0,-1):               #(4,0)
        print(" "*(r-j) + "* "*j)

print()

'''
dry run
when i = 1
" "*(4) + "* "*(1)
     *
when i = 2
" "*(3) + "* "*(2)
     * *
and so on
*  *  *  *

lower part

when j=4
" "*(1)
'''




# Sand glass pattern
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

r = 6
for i in range(1, r+1):
    print(" "*(i-1) +"* "*(r-i+1))
# lower part
for j in range(2,r+1):                 # (1,6)
    print(" "*(r-j)+"* "*j)

print()

# k shaped star pattern
# * * * * *
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *

r = 5
for i in range(r, 0 , -1):
     print("* "*i)
r=5
for j in range(2,r+1):
     print("* "*j)
print()

# Hexagon

#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *

r=5
for i in range(3, r+1):
     print(" "*(r-i)+"* "*i)

for j in range(3, r+1):
     print(" "*(r-j)+"* "*j)

print()

# hollow star pattern
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

r = 5
for i in range(1,r+1):
    if(i==1 or i==r):
      print("* "*r)
    else:
         print("* " + " "*(r-2) + "* ")

print() 

# hollow rectangle
# '''
# * * * * * * * * * * 
# *                 *    
# *                 *
# *                 *
# * * * * * * * * * *
r = 5 
c=10
for i in range(1,r+1):
    if(i==1 or i==r):
      print("* "*c)
    else:
         print("* " + " "*(r+3) + "* ")

print() 

