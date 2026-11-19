"""                                              Lists
|
|#List(value) - converts an iterable (sequence) into a list
|#Nested List - 2 or more lists inside 1 list
|#Matrix[] - row,column
|                      List: []
|                      Nested List: [[],[]] 
|                      Matrix:  0  1  2  
|                       row 0  [a][b][c]
|                       row 1  [d][e][f]
|                       row 2  [g][h][i]
|-Target entire row: matrix[1] | Target entire matrix: matrix 
|-Target specific: matrix[row][column] | Target multiple rows: [startRow:stopRow]
|-Target specific items in rows: [start][:end]
|
|How to create lists:
|                   -Empty
|                   -Manual
|                   -Nested
|How to Access & Read:
|                    -Indexing [a][b][c][d]
|                              [0][1][2][3]
|                     letters[3] or letters[-1]
|-Target multiple items: [start:stop]
|
|How to Unpack:
|How to Explore & Analyze:
|How to Change:
|How to Order:
|How to Copy:
|How to Combine:
|How to Iterate:
|How to Transform:
|How to Filter:
|
|
|
|
|
|
|
|
|
|
|
|
|
"""

'''                                    Lists'''

print("Lists")
empty = []
letters = ['a','b','c','d']
numbers = [1,2,3,4]

empty = list(letters) + list(numbers)
print(empty)

'''                                    Nested Lists'''

print("Nested Lists")
List1 = [["a","b","c","d"],
         [1,2,3,4]]

print(List1)

'''                                    How to Access & Read:'''

print('How to Access & Read:')
#normal list
lst = ['a','b,','c','d']
print(lst[-2])
print(lst[2])

#matrix
matrix = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]
print(matrix)
print(matrix[2])
print(matrix[2][1])
print(len(matrix))

#target multiple items
print(lst[:2])
#target multiple lists
print(matrix[:2])
#target multiple items in list
print(matrix[2][:2])

'''                                    How to Unpack:'''
print('How to Unpack:')
'''                                    How to Explore & Analyze::'''
print('How to Explore & Analyze:')
'''                                    How to Change:'''
print('How to Change:')
'''                                    How to Order:'''
print('How to Order:')
'''                                    How to Copy:'''
print('How to Copy:')
'''                                    How to Combine:'''
print('How to Combine:')
'''                                    How to Iterate:'''
print('How to Iterate:')
'''                                    How to Transform:'''
print('How to Transform:')
'''                                    How to Filter:'''
print('How to Filter:')