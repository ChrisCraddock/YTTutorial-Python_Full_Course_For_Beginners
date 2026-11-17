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