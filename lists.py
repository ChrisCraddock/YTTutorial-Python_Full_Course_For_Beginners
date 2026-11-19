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
|               -Add:
|                   -.append(): Add new value at end of list
|                   -.insert(): Add new value at start of row or with specified position (index,value) or for matrix: (index,[value])
|               -Update: Replace the position in the list and the value to replace with. Replace list entirely using blank [:] = 'value'
|                            -letters = ['a']
|                             letters[0] = 'b'
|                            -matrix[2] = ['x','y','z'] <--Target entire row
|                            -matrix[1][2] = '-' <--Target specific location
|               -Remove: Remove old, duplicate and/or bad data
|                   -.clear(): Remove ALL from list
|                   -.remove(): 
|                            - Remove 1st occurance in a list (value) 
|                            - Remove specified row from matrix matrix.remove(['a','b','c'])
|                            - Remove specified value from specified row from matrix matrix[1].remove('e')
|                   -.pop(): 
|                            - Remove by position or leave empty for last in list
|                            - Remove last row from matrix matrix.pop()
|                            - Remove specified value from specified row matrix[2].pop(0)
|
|How to Order:
|               -.sort(): - For sorting current list into a new list
|                            - default: from smallest to largest or A-Z.
|                            - (reverse = True) from largest to smallest or Z-A
|                            - Matrix: sorts by the 1st item of each row and then by the inner list
|               -sorted(): - For sorting current list into a new list
|                            - default: from smallest to largest or A-Z.
|               -.reverse(): - Reverse the order of the list
|               -reversed(): - Creates an iterator object, not a list
|               -list(reversed()): - Creates a reversed list of the iterator object
|
|
|How to Copy:
|               -Reference: If you use assignment (copy = original) any addition to new variable is reflected in original
|                            - 
|               -.copy(): Create seperate, indapendant list in memory
|                            - 
|               -Shallow Copy: .copy() on a matrix..but may reflect changes made in one list to the other list (same as copy.copy)
|                            - 
|               -Deep Copy: copy.deepcopy() Import Copy module. Does not reflect changes made in one list to the other list 
|               
|               -Note: copy.copy is more generaly that list.copy and not limited to lists
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
"""
#append
print('How to Change:')
letters = []
letters.append('a')
print(letters)
#insert
letters.insert(0,'b')
print(letters)


lists = ["a",2,"b",4]
print(lists)
lists.pop(2)
print(lists)
lists.remove('a')
print(lists)
lists.clear()
print(lists)

matrix = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]
print(matrix)
#matrix[1].pop(1)
#print(matrix)
matrix[1].remove('e')
print(matrix)
"""
'''                                    How to Order:'''
"""
print('How to Copy:')
letters = ['a','b']
letters[:] = 'c'
print(letters)

#Sorting
letters = ['c','r','n','a','b']
letters.sort()
print(letters)
letters.sort(reverse=True)
print(letters)

matrix = [
    ['d','h','c'],
    ['g','e','b'],
    ['a','f','i']
]
#Sorted
letters = ['c','r','n','a','b']
new_letters = sorted(letters)
print(new_letters)

matrix = [
    ['d','h','c'],
    ['g','e','b'],
    ['a','f','i']
]
new_matrix = sorted(matrix)
print(new_matrix)
[['a', 'f', 'i'],
 ['d', 'h', 'c'],
 ['g', 'e', 'b']]
"""
'''                                    How to Copy:'''

print('How to Copy')
#Reference
letters = ['a','b','c','d']
letters_copy = letters
letters_copy.append('z')
print(letters)
print(letters_copy)
#Copy
letters = ['a','b','c','d']
letters_copy = letters.copy()
letters_copy.reverse()
print(letters)
print(letters_copy)

#Shallow Copy
matrix = [['a', 'f', 'i'],
          ['d', 'h', 'c'],
          ['g', 'e', 'b']]
matrix_copy = matrix.copy()
print("original:",matrix)
print("copy:",matrix_copy)
matrix.pop()
print("original pop:",matrix)
print("copy:",matrix_copy)

matrix = [['a', 'f', 'i'],
          ['d', 'h', 'c'],
          ['g', 'e', 'b']]
matrix_copy = matrix.copy()
matrix_copy.pop()
print("original:",matrix)
print("copy pop:",matrix_copy)

matrix = [['a', 'f', 'i'],
          ['d', 'h', 'c'],
          ['g', 'e', 'b']]
matrix_copy = matrix.copy()
matrix[0].append('z')
print("original append:",matrix)
print("copy",matrix_copy)

matrix = [['a', 'f', 'i'],
          ['d', 'h', 'c'],
          ['g', 'e', 'b']]
matrix_copy = matrix.copy()
matrix_copy[0].append('z')
print("original:",matrix)
print("copy append:",matrix_copy)

#Deep Copy
import copy
matrix = [['a', 'f', 'i'],
          ['d', 'h', 'c'],
          ['g', 'e', 'b']]
matrix_copy = copy.deepcopy(matrix)
matrix_copy[0].append('z')
print("original:",matrix)
print("copy append:",matrix_copy)

'''                                    How to Combine:'''

print('How to Combine:')


'''                                    How to Iterate:'''

print('How to Iterate:')

'''                                    How to Transform:'''

print('How to Transform:')
'''                                    How to Filter:'''

print('How to Filter:')


