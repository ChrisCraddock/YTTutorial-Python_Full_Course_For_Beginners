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
|----------Types:
|#For -
|#While -
|
|----------Control:
|#break -
|#pass -
|#continue -
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
score = 50
submitted_project = True
if score >= 90:
    print('High')
else:
    print('Low')

if submitted_project:
    print('Submitted')
else:
    print('Not Submitted')

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