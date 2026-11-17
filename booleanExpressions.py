"""----------------------------------------------Boolean Expressions"""

"""                           Values
-True = if the value is non-empty or non-zero
-False = if the value is empty or zero
"""
"""                           Functions
-bool() - True/False
-any() - Returns True if ANY value is True
-all() - Returns True if ALL values are True
-isinstance()
"""
"""                           Comparison Operators
-==
-!=
-<
->
->=
-<=
"""
"""                           Logical Operators
-and
-or
-not
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
print(True) #True
print(False) #False
print(type(True)) #class 'bool'
print(bool(123)) #True
print(bool("Hi")) #True
print(bool(0)) #False
print(bool()) #False
print(bool("")) #False

'''                                    Functions'''
email = ""
phone = "0123-4567"
username = ""
#Allow registration if any field is filled
print(any([email,phone,username]))
#Allow registration if all fields are filled
print(all([email,phone,username]))