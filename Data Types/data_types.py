"""                                            Data Types"""
"""
Primitive/Core value types:
str() = String
bool() = Boolean {True/False}

-Numeric:
int() = Integer
float() = number with floating decimal point
complex = 3+5j

-Date/Time
date = date
time = time
datetime = date + time


Data structures/Collections/Containers:
list[] = holds multiple values [1,2,3]
dict() = holds multiple value pairs {'a':1,'b',2}
set() = holds multiple values {1,2,3}
tuple() = holds multiple values (1,2,3)
array = ('i',[10,20])

Dynamic: Data types can change at any time
Quotes turn numbers into strings
"""
a = 10 #int
b = 3.14 #float
c = "Hello" #string
d = 'Hi' #string
e = "1234" #string
f = True #boolean
g = False #boolean
h = None #no value
i = "" #blank string value
j = " " #empty string value

"""                                            Functions + Data Types"""

"""
3 types pf functions:
Standalone: print()/type()
Methods of class: upper()/replace()
Operations: + / >< == in or (behind the scenes)

Where do they come from?
-Standard library
-3rd Party Libraries
-User defined

Standard library: Built-in module {len(),type(),print()} | Class str {upper(), replace()} | Class int {to_byte()}
Math module: have to import {abs(),round(),floor}
"""

"""                                            Functions vs Methods"""
"""
Functions:
Independent block of code
Syntax: function_name(value)
Example:
print("Hello")
type(50)

Methods:
Functions belong to objects/classes
value.method_name()
Example:
'hello'.upper()
50.bit_length()
"""
text = "hi"
number = 10

print(text)
print(type(text))
print(len(text))
print(text.upper())

print(number)
print(type(number))
print("Bits needed to store number",number.bit_length())

"""
Challenge:
Create 5 variables - each with a different data type:
1. Age
2. Height (with decimals)
3. Name
4. Are you a student?
5. Something with no value yet

Then print the values, data types, lengths of all variables
"""