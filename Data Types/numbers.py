"""                                            Numbers"""
"""Types"""
#Int = whole numbers
#float = decimal numbers
#complex = real number + imaginary (advanced math / engineering / physics / science)
"""Math Operators"""
#+ - addition
#- - subtraction
#* - multiply
#/ - division
#// - floor division - dived 2 numbers and rounds down
#% - returns the leftovers (detect if numbers are even or odd)
#** - exponent - to the power of
#+= - increase variable by stated amount
#-= - decrease variable by stated amount
#*= - multiple by certain amount
"""Rounding"""
#abs() - absolute number, no negative sign
#round() - rounds number to the nearest EVEN number
#Math.ceil() - ceiling - rounds up
#Math.floor() - floor - rounds down
#Math.trunc() - truncate - cuts off the decimal part and keeps the whole number (no round)
"""Advanced Math"""
#sqrt() - square root
#sin() - calculates the sine of of a number,
#        where the input must be in radians and the output is a float between -1 and 1
#cos() - calculates the cosine of an angle x given in radians,
#        returning a float between -1 and 1
#log() - computers the natural logarithm
"""Random"""
#random() - returns a random float between 0.00 and 1.0
#randint() - a whole number from start to end (start,end)
"""Validation"""
#is_integer() - checks if whole number, does not count .0 as a float True/False
#isinstance() - checks if a value belongs to a certain data type (value, type) True/False

"""                                            Types"""
x = 5
y = 5.7
z = 2+3j
b = "24"
print("x is",x,f"which is {type(x)}")
print("float(x) is",float(x),f"which is {type(float(x))}")
print("y is",y,f"which is {type(y)}")
print("z is",z,f"which is {type(z)}")
print("b is",b,f"which is {type(b)}")
print("int(b) is",b,f"which is {type(int(b))}")

"""                                            Math Operators"""

print(1+1)
print(1-1)
print(1*2)
print(7/2)
print(7//2)
print(7%2)
print(7**2)

x = 2
x = x+3
x += 3

"""                                            Rounding"""

#Measure Distance
print(2-10)
print(abs(2-10))

#Rounding
price = 34.997863
print(price)
print(round(price))
print(round(3.5))
print(round(4.5))
print(round(price,3)) #specify how many decimals to remain

import math
print("Import Math")
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))

"""                                            Random"""
import random
print("Import Random")
print(random.random())
print(random.randint(-1000000000000000,1000000000000000))

"""                                            Float"""

#is_integer()
x = 7
t = 7.0
d = 7.1
print(x.is_integer())
print(t.is_integer())
print(d.is_integer())
#isinstance()
print(isinstance(x,int))
print(isinstance(t,float))
print(isinstance(d,str))