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

'''
error

'''

r = 5
for i in range(1,r+1):     #(1,6)
    print(" "*(r-i) + "* "*i)