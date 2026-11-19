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
|               -order of variables must match order of values. list1 = [spot1,spot2,spot3] spot1,spot2,spot3 = list1
|               - number of variables must match number of values unless using '*'
|               - you can unpack any sequence (lists,tuples,strings,etc.)
|               - _ can be used where you don't need to store a value
|How to Explore & Analyze:
|               -All(): True/False
|                   - 0, '' considered to be empty and give False, ' ' is not considered empty and will give True
|                   - True will give True and False will give False
|                   - None will create error
|               -Any(): True/False
|                   - Returns True if all values are True (0,1,'',' ',None,False,'a')
|               -Math: min/max/sum
|               -Method.count(): Count how many times a specificed value occurs. 
|                   - Example: numbers = [1,2,3,4,5,6] numbers.count(5)
|               -Method.index(): Returns the position of the 1st occurrence of a value. 
|                   - Example: numbers = [1,2,3,4,5,6] numbers.index(5)
|               -In: Check if value does exists in a sequence. True/False
|               -Not In: Check if value does not exists in a sequence. True/False
|               -Comparison: <, > The first elements are compared, if they are equal then moves on to next element
|               -Is: checks stored memory adress, not list itself
|How to Change:
|               -Add
|               -Update
|               -Remove
|
|How to Order:
|
|
|How to Copy:
|
|
|How to Combine:
|
|
|How to Iterate:
|
|
|How to Transform:
|
|
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
|
|
"""

'''                                    Lists'''
"""
print("Lists")
empty = []
letters = ['a','b','c','d']
numbers = [1,2,3,4]

empty = list(letters) + list(numbers)
print(empty)
"""
'''                                    Nested Lists'''
"""
print("Nested Lists")
List1 = [["a","b","c","d"],
         [1,2,3,4]]

print(List1)
"""
'''                                    How to Access & Read:'''
"""
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
"""
'''                                    How to Unpack:'''
"""
print('How to Unpack:')
person = ['Maria',29,'data engineer','spain']
name = person[0]
age = person[1]
role = person[2]
country = person[3]

name,age,role,country = person
print(name)
name,_,role,_ = person
print(role)
"""
'''                                    How to Explore & Analyze::'''
"""
print('How to Explore & Analyze:')
numbers = [1,5,2,4,3,True,' ']
#print("max:",max(numbers))
#print("min:",min(numbers))
#print("sum:",sum(numbers))

print("All:", all(numbers)) #True/False
print("Any:", any(numbers)) #True/False
print("Count:", numbers.count(5))
print("Index:",numbers.index(3))

print(4 in numbers)
"""
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


