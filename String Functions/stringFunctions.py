""""
Types:
-type()
-str()

Math:
-len()
-count()

Transformations:
-replace()
- +
-f{}
-split()
- *
--Extraction:
-[]
[#:#]

Cleaning:
--Clean Whitespaces:
-lstrip()
-rstrip()
-strip()
--Clean Cases
-lower()
-upper()

Search:
-startswith()
-endswith()
-find
-in

Validation:
-isalpha()
-isnumeric()
"""

#-----------------------------------------------Types

#---------------------Type()
name = "Me"
print(type(name))

age = 40
print(type(age))
#print("Your age is:"+age)

#---------------------Str()
print("Your age is: "+str(age))

#-----------------------------------------------Math

#---------------------Len()
password = "123a"
print(len(password))

text= """Line 1
Line 2
Line 3"""

#---------------------Count()
print(text.count("Line"))

#-----------------------------------------------Transformations

#---------------------Replace()
price = "1234,56"
print(price.replace(",","."))
phone = "123-456-7890"
print(phone.replace("-","/"))

price = "$1,299.99"
print(type(price),price.replace("$","").replace(",",""))

"""
Challenge:
Convert the messy phone number into a clean number format with only digits
"+49 (176) 123-4567"
"""
phoneNumber = "+49 (176) 123-4567"

print(phoneNumber.replace('"',"").replace("+","00").replace("(","").replace(")","").replace(" ","").replace("-",""))

#--------------------- +
first_name = "Michael"
last_name = "Scott"
full_name = first_name +" "+ last_name
print(full_name)

folder = "C:/users/me/"
file = "report.csv"
full_path = folder+file
print(full_path)

#---------------------F-String (formatted)
name = "Sam" #str
age = 34 #int
is_student = False #bool
print(f"My name is {name}, {age} years old, student status is {is_student}.")
print(f"2+3={2+3}")
print(f"{{This is me}}")

#---------------------Split
stamp = "2026-09-20 14:30"
print(stamp.split(" "))

#--------------------- *
print("ha " * 3)
print("=" * 9)

#---------------------Indexing & Slicing

"""
-negative index starts at end of line
-5-4-3-2-1
 h e l l o
 0 1 2 3 4
+positive index starts at front of line starting at 0
"""
indexing = "python"
print(f"The length of {indexing} is {len(indexing)}")
#slicing - [start:end] [included:not included]
print(indexing[0])
print(indexing[-5])
#open-ended slicing - [1:]
print(indexing[0:])
#step slicing - [start:end:step]
print(indexing[0:5:2])

slicing = "2026-09-20"
#extract year
print(slicing[0:4])
print(slicing[:4])
#extract month
print(slicing[5:7])
#extract day
print(slicing[8:])