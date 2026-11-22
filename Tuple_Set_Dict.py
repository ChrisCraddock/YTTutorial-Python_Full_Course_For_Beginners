'''                                            Tuples / Sets / Dictionaries
|
|Can Be: | Ordered | Duplicates | Indexed | Mutable |  
|list[]  |    Y    |     Y      |    Y    |    Y    |     
|tuple() |    Y    |     Y      |    Y    |    -    |
|set{}   |    -    |     -      |    -    |    Y    |
|dict{}  |    Y    |     -      |    Y    |    Y    |
|
|
|Tuple:
|                   -Ordered collection that can't be changed after creating it
|                   -Use ()
|                   -convert to list by using ways such as newVar = sorted(tuple)
|                   -Use to protect values
|
|===================================================================================================================|
|
|Sets:
|                   -Unordered Collection of Unique Values
|                   -Use {}
|                   -Set is unordered (does not keep the same way it was put in)
|                   -No duplicates values (unique) or indexable
|                   -Uses hash function to store the contents in random order
|                   -Reason: speed
|
|
|
|==================================================================================================================|
|Set Operators:
|                   -.add() - only add items if not a duplicate
|                   -.update() - Merges another group of values (iterable) into the set
|                   -Use math operators as quick shortcuts: |= & - ^ 
|                   -.remove() - throws Error if value does not exist
|                   -.discard() - does not throw Error if value does not exist
|                   -.pop() - removes random item from set
|
|                   - |= (update): Adds elements from another set.
|                   - Union (| or union()): Combines all unique elements from both sets
|                       -print(a.union(b)) #returns a new set, leaving original untouched
|
|                   - &= (intersection_update): Returns only common/shared elements.
|                   - Intersection (& or intersection()): Returns elements present in both sets
|                       -print(a.intersection(b)) #does not alter the original sets later on
|                       -print(a.intersection_update(c)) #Returns None, permanently changes the set it is called on
|
|                   - -= (difference_update): Removes elements found in another set.
|                   - Difference (- or difference()): Returns elements in the first set but not in the second
|                       -print(a.difference(b)) #does not alter the original sets later on
|                       -print(a.difference_update(c)) #Returns None, permanently changes the set it is called on
|
|                   - ^= (symmetric_difference_update): Removes common elements, keeping unique ones.
|                   - Symmetric Difference (^ or symmetric_difference()): Returns elements in either set, but not in both
|                       -print(a.symmetric_difference(b)) #does not alter the original sets later on
|                       -print(a.symmetric_difference_update(c)) #Returns None, permanently changes the set it is called on
|
|                   - Subset (<= or issubset()): Checks if all elements of the left set are in the right set. True/False
|                   - Proper Subset (<): Checks if the left set is a subset and not equal to the right set. True/False
|                   - Superset (>= or issuperset()): Checks if the left set contains all elements of the right set. True/False
|                   - Proper Superset (>): Checks if the left set is a superset and not equal to the right set. True/False
|                   - Equality (== / !=): Compares if sets contain the exact same elements. True/False
|                   - Disjoint (.isdisjoint(): Returns True if both sets share no overlapping items)
|==================================================================================================================|
|Dictionary:
|                   - Store data in key value pairs
|                   - {key:value}
|                   - Ordered
|                   - No Duplicates - last key replaces 1st key occurance, duplicate values are allowed
|                   - Not Indexed but can be accessed by using their keys
|                   - Mutable BUT must access using the key
|==================================================================================================================|
|Special Methods
|                  - Access:
|                   - .get(): Prints None if key value not found.
|                       - Can customize return if not found. Ex: ('name','Unknown')
|                  -Checks:
|                   - in/not in
|                  -View Objects:
|                   -.keys(): return all the keys in the dictionary
|                   -.values(): return all the values in the dictionary
|                   -.items(): return all the key/value pairs in the dictionary
|                       -use for looping, transforming, new dict building, compairing etc..
|
|                   -Add: variable_name['newKey'] = 'value'
|                   -Update: variable_name['existingKey'] = 'value'
|                   -.update(): add/update keys using another dictionary
|                   -Remove:
|                   -.pop(): must specify key. Removes both key/value pair
|                       - Can customize return if not found. Ex: ('name','Unknown')
|                   -.popitem(): returns and deletes the most recent key/value pair added
|                   -Creation:
|                   -dict.fromkeys(): Builds a new dictionary where all kets get the same default value.
|                       - Ex: user = dict.fromkeys(['key1', etc..],None) #Can other constant value 
|==================================================================================================================|
|User Case:
|                   -Mapping translations to friendly values
|                   -Mapping Abbreviations
|                   -Databases or API Records
|                   -ETL and Pipeline Settings
|                   -Metadata
|==================================================================================================================|
'''
'''                                    Lists'''
"""
#Ordered
my_list = [10,30,20]
print(my_list)

#Duplicates
my_list = [10,30,20,10]
print(my_list)

#Indexed
my_list = [10,30,20]
print(my_list[1])

#Mutable
my_list = [10,30,20,10]
my_list[3] = 40 #replace
print(my_list)
"""
'''                                    Tuples'''
"""
#Ordered
my_tuple = (10,30,20)
print(my_tuple) #Keeps ordered

#Duplicates
my_tuple = (10,30,20,10)
print(my_tuple)

#Indexed
my_tuple = (10,30,20,10)
print(my_tuple[1])

#Not Mutable - tuple uses () while lists use []
my_tuple = (10,30,20,10)
#my_tuple[3] = 50
print(my_tuple)
conversion = sorted(my_tuple) #convert from tuple to a list
conversion[3] = 50
print(conversion)
"""
'''                                    Sets'''
"""
#Unordered
my_set = {10,30,20,40,900,60,782,500}
print(my_set)

#No Duplicates
my_set = {10,30,30}
print(my_set)

#Not Indexed

#Mutable
my_set = {10,30,30}
my_set.remove(30)
print(my_set)
"""
'''                                    Sets Operators'''
"""
#.add - only add items if not a duplicate
my_set = {10,20,30,40}
my_set.add(50)
print(my_set)

#.update - Merges another group of values (iterable) into the set
my_set = {10,20,30,40}
my_set.update('hi')
my_set.update([3],[40],[4,5,6],{1,2})
print(my_set)

#Use math operators as quick shortcuts: |= & - ^
my_set = {10,20,30,40}
my_set |= {50} #add value
my_set.remove(50) #throws error if value does not exist
my_set.discard(50) #does not throw error
my_set.pop() #removes random item from set
print(my_set)
"""
'''                                    Sets Operators(Special)'''
"""
#|= (update): Adds elements from another set.
#Union (| or union()): Combines all unique elements from both sets
a = {10,20,30,40}
b = {30,40,50,60}
print(a.union(b)) #returns a new set, leaving original untouched
print(a|b)
====================
#&= (intersection_update): Returns only common/shared elements.
#Intersection (& or intersection()): Returns elements present in both sets
a = {10,20,30,40}
b = {30,40,50,60}
c = {30,40,50,70}
b & c
print(b)
print(a.intersection(b)) #does not alter the original sets later on
print(a.intersection_update(c)) #Returns None, permanently changes the set it is called on
print(a)
print(c)
====================
#-= (difference_update): Removes elements found in another set.
#Difference (- or difference()): Returns elements in the first set but not in the second
a = {10,20,30,40}
b = {30,40,50,60}
c = {30,40,50,70}
c-a
print(c)
print(a.difference(b)) #does not alter the original sets later on
print(a)
print(a.difference_update(c)) #Returns None, permanently changes the set it is called on
print(a)
====================
#^= (symmetric_difference_update): Removes common elements, keeping unique ones.
#Symmetric Difference (^ or symmetric_difference()): Returns elements in either set, but not in both
a = {10,20,30,40}
b = {30,40,50,60}
c = {30,40,50,70}
c^a
print(c)
print(a.symmetric_difference(b)) #does not alter the original sets later on
print(a)
print(a.symmetric_difference_update(c)) #Returns None, permanently changes the set it is called on
print(a)
====================
#Subset (<= or issubset()): Checks if all elements of the left set are in the right set. True/False
a = {10,20,30,40}
b = {30,40,50,60}
print(a.issubset(b))
print(a<=b)
====================
#Proper Subset (<): Checks if the left set is a subset and not equal to the right set. True/False
a = {10,20,30,40}
b = {30,40,50,60}
print(a<b)
====================
#Superset (>= or issuperset()): Checks if the left set contains all elements of the right set. True/False 
a = {10,20,30,40}
b = {30,40,50,60}
print(a.issuperset(b))
print(a>=b)
====================
#Proper Superset (>): Checks if the left set is a superset and not equal to the right set. True/False
a = {10,20,30,40}
b = {30,40,50,60}
print(a>b)
====================
#Equality (== / !=): Compares if sets contain the exact same elements. True/False
a = {10,20,30,40}
b = {30,40,50,60}
print(a==b)
print(a!=b)
====================
#Disjoint (.isdisjoint(): Returns True if both sets share no overlapping items)
a = {10,20,30,40}
b = {30,40,50,60}
print(a.isdisjoint(b))
"""
'''                                    Dictionary'''
"""
#Ordered
my_dict = {
    'a':10,
    'b':20,
    'c':30
}
print(my_dict)

#No Duplicates - last key replaces 1st key occurance, duplicate values are allowed
my_dict = {
    'a':10,
    'b':20,
    'c':30,
    'd':30
}
print(my_dict)

#Not Indexed but can be accessed by using their keys 
my_dict = {
    'a':10,
    'b':20,
    'c':30
}
#print(my_dict[1])
print(my_dict['a'])

#Mutable BUT must access using the key
my_dict = {
    'a':10,
    'b':20,
    'c':30,
    'd':30
}
my_dict['c'] = 80
print(my_dict)
"""
'''                                    Dictionary Methods(Special)'''
"""
#Access:
user = {'id':1, 'age':30,'city': 'berlin'}
#if the key is not found, throws Keyerror
print(user['id'])
print(user.get('name')) #gives None if key not found

#Check
print('age' in user)

#View Objects
print(user.keys())
#View Values
print(user.values())
#View Key/Value
print(user.items())

#Looping
for u in user.items():
    print(u)
#-or-
for key, value in user.items():
    print(key, value)

#Add
user['name'] = 'John'
#Update
user['age'] = 35
user.update({'age':40, 'city':'paris'})
#Remove
user.pop('age') #removes key and value
print(user.popitem())
print(user)

#Creation
user1 = {
    'id': None,
    'name': None,
    'age': None,
    'city': None,
}
#-or-
user2 = dict.fromkeys(['id','name','age','city'],None)
print(user2)
"""
'''                                    Challenge'''
"""
user = {
    'id': 1,
    'name': 'John',
    'age': 30,
    'city': 'Berlin',
}
# 1) Create new Dict
# 2) Keep only key/value pairs with String values
# 3) Convert values to Uppercase
# 4) Use elegant and short solution
"""

