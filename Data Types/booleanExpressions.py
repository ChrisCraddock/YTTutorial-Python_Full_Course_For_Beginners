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

-in - Check if a value is inside another value (string, list tuple or other sequence) True/False
-not in - Check if a value is not inside another value (string, list tuple or other sequence) True/False
"""
"""                           Identity Operators
-is - Check if 2 variables refer to the same object in memory True/False
-is not - Check if 2 variables do not refer to the same object in memory True/False
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

#By default AND has higher execution order than OR
#Use () to control execution priority
print(5==5 or 8>5 and 6<4)
print((5==5 or 8>5) and 6<4)

"""
Challenge:
1-Check if a user's name is NOT empy and the age is greater than or equal to 18
2-Check if the password is atleast 8 characters long and does NOT contain spaces
3-Check if a user's email contains '@', ends with'.com' and is NOT empty
4-Check if a username is a string, is NOT None and is longer than 5 characters
5-Check if the user is either an admin or a moderator, and either they're not banned or they've verified their email.
"""
username = "BobbleHead82"
age = 24
email = 'bobble82@gmail.com'
permissions = 'Moderator'
activity = 'Active'
emailVerified = 'Verified'

print("Challenge")
usernameCheck = isinstance(username,str) is not None and len(username) > 5
ageCheck = age >= 18
passCheck = len(username) == len(username.strip())
emailCheck = '@' in email and '.com' in email and len(email) > 5
access = (permissions == 'Administrator' or 'Moderator') and (activity != 'Banned') and emailVerified == 'Verified'
print(usernameCheck == ageCheck == passCheck == emailCheck == access)
print(usernameCheck)
print(ageCheck)
print(passCheck)
print(emailCheck)
print(access)

'''                                    Membership Operators'''
print('Membership Operators')
#in
emailCheck = '@' in email and '.com' in email and len(email) > 5
print(emailCheck)
#not in
emailCheck2 = '$' not in email
print(emailCheck2)

'''                                    Identity Operators'''
print('Identity Operators')
#is
a = [1,2,3]
b = [1,2,3]
c = 5
d = 5
e = 'a'
f = 'b'
print(a is b) #False
print(c is d) #True
print(id(a)) #Memory Location
print(id(b)) #Memory Location
print(id(d)) #Memory Location
print(id(c)) #Memory Location
#is not
print(a is not b) #True
print(c is not d) #False
print(id(a)) #Memory Location
print(id(b)) #Memory Location
print(id(d)) #Memory Location
print(id(c)) #Memory Location