# 10-02-2026 after starpattern

'''
Docstring for Looping.Patterns.numberpattern

1. Right-angled Number Triangle
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
2. Inverted Right-angled Number Triangle  
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
3. Right-aligned Number Triangle
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
4. Pyramid of Same Numbers
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
5. Floyd's Triangle
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
6. Left-aligned Descending Numbers
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
7. Number Pyramid (Floyd's Triangle with alignment)
    1
   2 3
  4 5 6
 7 8 9 10
11 12 13 14 15
'''


# 1. Right-angled Number Triangle
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n=5
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()

'''

dry run
when row =1 ; col = (1,2)
1
when row = 2 ; col = (1,3)
1 2
when row = 2 ; col = (1,4)
1 2 3

and so on
1 2 3 4 5
'''


3. Right-aligned Number Triangle
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5


n=5
for r in range(1, n+1):
    for c in range(1,r+1):      #(5-1) -> 4
        print(c,end=" ")      
    print()
