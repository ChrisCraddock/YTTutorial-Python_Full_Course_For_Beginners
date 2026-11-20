'''                                            String Functions
|
|Types:
|               -type()
|               -str()
|===================================================================================================================|
|Math:
|               -len()
|               -count()
|===================================================================================================================|
|Transformations:
|               -replace()
|               -+
|               -f{}
|               -split()
|               - *
|               -Extraction:
|                   -[]
|                   -[#:#]
|===================================================================================================================|
|Cleaning:
|                   -Clean Whitespaces:
|                       -lstrip()
|                       -rstrip()
|                       -strip()
|                   -Clean Cases
|                       -lower()
|                       -upper()
|===================================================================================================================|
|Search:
|                   -startswith()
|                   -endswith()
|                   -find
|                   -in
|===================================================================================================================|
|Validation:
|                   -isalpha()
|                   -isnumeric()
|===================================================================================================================|
'''

"""                                            Types"""

# ---------------------Type()
name = "Me"
print(type(name))

age = 40
print(type(age))
# print("Your age is:"+age)

# ---------------------Str()
print("Your age is: "+str(age))

"""                                            Math"""

# ---------------------Len()
password = "123a"
print(len(password))

text = """Line 1
Line 2
Line 3"""

# ---------------------Count()
print(text.count("Line"))

"""                                            Transformations"""

# ---------------------Replace()
price = "1234,56"
print(price.replace(",", "."))
phone = "123-456-7890"
print(phone.replace("-", "/"))

price = "$1,299.99"
print(type(price), price.replace("$", "").replace(",", ""))

"""
Challenge:
Convert the messy phone number into a clean number format with only digits
"+49 (176) 123-4567"
"""
phoneNumber = "+49 (176) 123-4567"

print(phoneNumber.replace('"', "").replace(
    "+", "00").replace("(", "").replace(")", "").replace(" ", "").replace("-", ""))

# --------------------- +
first_name = "Michael"
last_name = "Scott"
full_name = first_name + " " + last_name
print(full_name)

folder = "C:/users/me/"
file = "report.csv"
full_path = folder+file
print(full_path)

"""                                            F-String (formatted)"""
name = "Sam"  # str
age = 34  # int
is_student = False  # bool
print(f"My name is {name}, {age} years old, student status is {is_student}.")
print(f"2+3={2+3}")
print(f"{{This is me}}")

# ---------------------Split
stamp = "2026-09-20 14:30"
print(stamp.split(" "))

# --------------------- *
print("ha " * 3)
print("=" * 9)

# ---------------------Indexing & Slicing

"""
-negative index starts at end of line
-5-4-3-2-1
 h e l l o
 0 1 2 3 4
+positive index starts at front of line starting at 0
"""
indexing = "python"
print(f"The length of {indexing} is {len(indexing)}")
# slicing - [start:end] [included:not included]
print(indexing[0])
print(indexing[-5])
# open-ended slicing - [1:]
print(indexing[0:])
# step slicing - [start:end:step]
print(indexing[0:5:2])

slicing = "2026-09-20"
# extract year
print(slicing[0:4])
print(slicing[:4])
# extract month
print(slicing[5:7])
# extract day
print(slicing[8:])

"""                                            Cleaning"""

# ---------------------Clean Whitespaces
# lstrip() strip white spaces from the left
# rstrip() strip white spaces from the right
# strip() strip white spaces from both sides

text = " Left Strip"
print(text.lstrip())
text = "Right Strip "
print(text.rstrip())
text = " Strip "
print(text.strip())
text = "###Strip###"
print(text.strip("#"))
# check for white spaces
text = "Strip "
print(len(text))
print(len(text.strip()))
print(len(text)-len(text.strip()))

"""                                            Case Conversion"""
# lower()
# upper()
text = 'WoRdS'
print(f"Using '.lower()' {text.lower()}")
print(f"Using '.upper()' {text.upper()}")

'''
Challenge:
Turn the messy string into a single clean summary with the name, role and age
"968-Maria, ( D@t@ Engineer );; 27y  "
'''
info = "968-Maria, ( D@t@ Engineer );; 27y  "

id = info[:3]
fname = info[4:9]
age1 = info.strip()
age2 = age1[-3:]
job1 = info.replace("@", "a")
job2 = job1[13:26]
print(age2)
print(
    f"This is {fname}, her employee id is {id}, she is a {job2} and is {age2}.")

"""                                            Search"""

# Startswith() - True/False
# endswith() - True/False
text = "A or B"
print(text.startswith('A'))
print(text.endswith('B'))

# find() - specific starting position starting from 0
print(text.find('or B'))

# in - to search for specific value True/False
print('or' in text)

if text.startswith('A') and text.endswith('B')  == True:
    print("Both are True")
else:
    print("No")

phone1 = "+48-176-12345"
phone2 = "48-176-12345"
phone3 = "0048-176-12345"
print(phone1[4:])
print(phone2[3:])
print(phone1.find("-"))
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])

"""                                            Validation"""
#isalpha() - check if str has only letters True/False
#isnumeric() - check if str has only numbers True/False

text1 = "USA"
text2 = "U$@"
print(text1.isalpha())
print(text2.isalpha())

text3 = "1234"
text4 = "1se4"
text5 = "12.34"
print(text3.isnumeric())
print(text4.isnumeric())
print(text5.isnumeric())