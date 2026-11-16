#-------------------------------------------------------------Variables

print("line 1")
print("line 2")
print("line 3")

name1 = "line 1"

print("this is", name1)
print(name1, "this is")
print("this", name1, "not 3")

"""
Challenge:
Print the following thre lines and add a variable to make it dynamic.
-info@something.com
-support@something.com
-www.something.com
"""
link = str('info@something.com')
print("Contact:",link)
link = str('support@something.com')
print("Contact:",link)
link = str('www.something.com')
print("Contact:",link)
#-------------------------------------------------------------Input

#Ask user their name and store inside variable
name = input("Input your name: ")
print("Hello,",name)

#-------------------------------------------------------------Print

# Functions: Accept input and give output
"""
3 types of functions:
Built-in Python
3rd-party Libraries
User Defined
"""
print("Double Quotes")
print('Single Quotes')

"""
Special Characters:
-Escape Sequences:
\' = include single quote in text
\" = include double quotes in text
\\ = include backslash in text
\n = new line
\t = tab
\b = backspace
Python will always expect some after a single backslash
"""

print("Double \"Quote\"")
print('Single \'Quotes\'')
print("Path: C:Home\\Desktop\\main.py")

"""
Challenge: 
-Use PRINT() to recreate this exact output
-You are allowed to use only one PRINT()
Your Learning Path:
    - Python Basics
    - Data Engineering
    - AI
"""

print("Your Learning Path:\n\t- Python Basics\n\t- Data Engineering\n\t- AI")

print("Your Learning Path:" \
"\n\t- Python Basics" \
"\n\t- Data Engineering" \
"\n\t- AI")

print("""Your Learning Path:
\n\t- Python Basics
\n\t- Data Engineering
\n\t- AI""")