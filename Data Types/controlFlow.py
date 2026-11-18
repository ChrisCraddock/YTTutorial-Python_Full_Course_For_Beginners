"""----------------------------------------------Control Flow"""

"""                           Conditional Statements
|-Check if condition is True or False and proceed accordingly
|#if - Define 1st condition
|      - only 1 'if' per statement
|      - must start with 'if'
|      - is required but can stand alone 
|#else - Runs only if all previous conditions are False. 
|        - Must come at end of statement
|        - does not require condition
|        - optional
|        - cannot stand alone
|        - only 1 else
|#elif - {if-elif-else} Asks a follow-up question, Only runs if previous conditions were false.
|        - Only comes after 'if'
|        - allowed to have multiple 'elif'
|        - needs codition
|        - cannot stand alone
|        - optional
|#Nested 'if' - 'if' statement inside another 'if'. Each 'if' can be followed by 'else'
|               - Python evalutes Boolean conditions directly, avoid explicit comparisons == True or == False  
|                 -example- variable: 
|#Independent if-else - Each 'if' is checked separatley, no dependancy
|                              Loops
|#One-Line if-else - Conditions on one line. 
|                       Example: score = 100
|                                'A' if score >= 90 else 'F'
|                                'A' if score >= 90 else 'B' if score >= 80 else 'F'
|Use Case: Simple Logic -> Inline-if / Complex Logic -> Classical-if
|#Case-Match - Evaluates a value against multiple values. Runs the code of the first match. Use '|' to check multiple values
|                       Example: country = 'Japan'
|                                match country:
|                                    case 'Japan'
|                                        print('JP')
|                                    else _: #the '_' = 'default to'
|                                        print('Ukn')
|----------Types:
|#For - Go through a group of items 1-by-1 to do something for each item
|                       Example: for i(loop vairable) in (1,2,3){sequence}:
|                                    print(i)
|       - takes the sequence and puts into memory an iterator: an object that goes through 1-by-1 in a sequence
|                       Example: [1][2][3]
|Use Case: 
|          - aggregate data like sum, count or avg
|          - transform data (cleaning) before processing {clean BEFORE manipulating}
|#While - Repeat block of code over and over While condition is True
|
|----------Control:
|#break - When to STOP. Stops the loop immediately
|#pass - When to SKIP. Does not matter if condition met, used as placeholder. Should not be in final
|#continue - When to PASS. Skips 1 loop cycle without stopping the loop {Use if condition is not critical}
|
|----------Else in for-loop:
|Runs a block of code only if the loop finished naturally
|Unlike 'if'-loop, 'else' executes every time at the end
|Useless unless used WITH a Break. Used to detect if interruption occured.
|  Example:
|     items = [1,2,3,4]
|     for i in items:
|         if i % 2 == 0:
|            print(f"Even number found: {i}")
|     else:
|         print("All numbers are odd.")
|
|----------Nested:
|#Inner Loop - Runs after outerloop's 1st run and then, when finished, back to the outer loop
|#Outer Loop - Runs 1st and then inner loop until finished and then 1 more outer lopp
|
|Case:
|     - Compare Lists
|     - Navigate Hierarchy/Layers|
"""

'''                                    Conditional Statement'''

#if
score = 100
if score >= 19:
    print("A")
#else
score = 100
if score <= 19:
    print("A")
else:
    print('B')
#elif
score = 100
if score <= 20:
    print('A')
elif score <= 50:
    print('B')
elif score <= 80:
    print('C')
else:
    print('D')
#Nested if
score = 50
submitted_project = True
if score <=90:
    if submitted_project:
        print("A+")
    else:
        print('A')
#Independent if-else
score = 91
submitted_project = True
if score >= 90:
    print('High')
else:
    print('Low')

if submitted_project:
    print('Submitted')
else:
    print('Not Submitted')
#One-line if-else
print('A' if score >= 90 else 'F')
grade = 'A' if score >= 90 else 'B' if score >= 80 else 'F'
print(grade)
#Match Case
country = 'India'
if country == 'United States':
    print('US')
elif country == 'India':
    print('IN')
elif country == 'Germany':
    print('DE')
elif country == 'Russia':
    print('RU')
elif country == 'Japan':
    print('JP')
else:
    print("Unk")

country = 'Japan'
match country:
    case 'United States'|'USA':
        print('US')
    case 'India':
        print('IN')
    case 'Germany':
        print('DE')
    case 'Russia':
        print('RU')
    case 'Japan':
        print('JP')
    case _:
        print("Unk")
"""
Challenge #1
Validate the quality and correctness of Email Values
-Must NOT be empty
-Must contain '.' AND '@'
-Must contain exactly one '@' symbol
-Must end with '.com', '.org' or '.net'
-Must not be longer than 254 characters
-Must start AND end with a letter or digit
"""
print('challenge #1:')

"""
Challenge #2
Validate the quality and correctness of Passwords
-Must NOT be empty
-Must be atleast 8 characters long
-Must include atleast 1 uppercase and 1 lowercase letter
-Must NOT be the same as the email
-Must NOT contain any spaces
-Must start AND end with a letter or digit
"""
print('challenge #2:')
'''                                    Loops'''

print("Loops")
#For
for i in (1,2,3,4,5):
    print(f"Round: {i}")
items = (1,2,3,4,5)
spacecrafts = [7,8,9,10]
for spacecraft in items:
    print(f"Round: {spacecraft}")
for items in spacecrafts:
    print(f"Round: {items}")
#---range(start{optional},stop,step{optional})
for i in range(10): #starts counting at 0 
    print(i)
for i in range(1,10): #starts counting at 1 and stops but not display 10
    print(i)
for i in range(1,10,4): #starts counting at 1, stops but not display 10, display every 4th numbers
    print(i)

"""
Challenge #3
Print the 7-times table from 1 to 10 using a 'for' loop
"""
print('challenge #3:')
number = 7
for num in range(1,11):
    number = num
    print(f"7 * {num} =",7*number)
    number *= num

"""
Challenge #4
Print a left-aligned pyramid of stars with 6 rows using a for-loop
"""
print('challenge #4:')
stars = 6
for star in range(1,stars+1):
    for j in range(star):
        print('*', end=' ')
    print()
   
#While

'''                                    Control'''
print("Control:")
#Break
names = ['john','maria','','kumar']
for name in names:
    print(f"Name= {name}")

for name in names:
    if name == '':
        print('Empyt value')
        break
    print(f"Name= {name}")

#Continue
names = ['john','maria','','kumar']
for name in names:
    if name == '':
        print("Empyt Value")
        continue
    print(f"Name= {name}")

#Pass
names = ['john','maria','','kumar']
for name in names:
    if name == '':
        pass #todo: Handle later
    print(f"Name= {name}")

emails = [
    'data@data.com',
    'scam@user.net',
    'DROP TABLE USERS;',
    'steve@gmail.com'
]
for email in emails:
    if email.endswith(';'):
        continue
    print(f"Email: {email}")

items = [1,2,3,4]
for i in items:
    if i % 2 == 0:
        print(f"Even number found: {i}")
        break
else:
    print("All numbers are odd.")

"""
Challenge #5
Check whether any filename appears more than once:
file_list = [
'report.csv',
'data.xlsx',
'summary.docx',
'report.csv',
'data'.csv'
]
"""
file_list = [
'report.csv',
'data.xlsx',
'summary.docx',
'report.csv',
'data.csv'
]
file_checked = []

for file in file_list:
    if file not in file_checked:
        file_checked.append(file)
        print(file_checked)
    else:
        print('Duplicate found')
        break
print(file_checked)

for x in (1,2,3):
    for y in (1,2):
        print(x,y)

'''                                    Nested Loop'''

for x in range(3):
    for y in range(2):
        for z in range(4):
            print(f"({x}as X, {y}as Y, {z}as Z)")

year = [2026,2027]
months = ['Jan','Feb']
days = range(1,26)

for y in year:
    for m in months:
        for d in days:
            print(f"{y}-{m}-{d}")

'''                                    While Loop'''
i = 1
while i<4:
    print(i)
    i += 1

attempt = 0
while attempt < 3:
    answer = input("Yes or No: ")
    if answer.lower() == "yes":
        print("cool")
        break
    attempt += 1
else:
    print("Bummer")

