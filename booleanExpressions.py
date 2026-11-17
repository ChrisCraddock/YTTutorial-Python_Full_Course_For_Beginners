"""----------------------------------------------Boolean Expressions"""

"""                           Values
-True = if the value is non-empty or non-zero
-False = if the value is empty or zero
"""
"""                           Functions
-bool() - True/False
-any() - Returns True if ANY value is True
-all() - Returns True if ALL values are True
-isinstance() - checks if a value belongs to a certain data type (value,type)
"""
"""                           Comparison Operators
Compare string values alphabetically
1x = is for assigning variables
-== - is equal to
-!= - is not equal to
-< - less than
-> - greater than
->= - greater than or equal to
-<= - less than or equal to
"""
"""                           Logical Operators
By default AND has higher execution order than OR
Use () to control execution priority
-and - Both must be True
-or - Atleast 1 must be True, All False = False
-not - Reverses False to True and True to False
"""
"""                           Membership Operators
-in
-not in
"""
"""                           Identity Operators
-is
-is not
"""

'''                                    True/False'''
#True = if the value is non-empty or non-zero
#False = if the value is empty or zero
print("True/False")
print(True) #True
print(False) #False
print(type(True)) #class 'bool'
print(bool(123)) #True
print(bool("Hi")) #True
print(bool(0)) #False
print(bool()) #False
print(bool("")) #False

'''                                    Functions'''

print("Functions")
email = ""
phone = "0123-4567"
username = ""
#Allow registration if any field is filled
print(any([email,phone,username]))
#Allow registration if all fields are filled
print(all([email,phone,username]))
#Check if value is a int
print(isinstance(123,int))

'''                                    Comparison Operators'''

print("Comparison Operators: True/False")
#==
print(8 == 8)
#!=
print(8 != 8)
#<
print(len('hello') < 8)
#>
print(len('hello') > 8)
#>=
print(len('bye') >= 8)
#<=
print(len('bye') <= 8)

'''                                    Logical Operators'''

print("Logical Operators: True/False")
#and
print(2>1 and 3>0)
#or
print(2>1 or 3>8)
#not
print(not 3>2)
print(3>2)
print(not 2>3)
print(2>3)
