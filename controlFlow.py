"""----------------------------------------------Control Flow"""

"""                           Conditional Statements
-Check if condition is True or False and proceed accordingly
#if - Define 1st condition
      - only 1 'if' per statement
      - must start with 'if'
      - is required but can stand alone 
#else - Runs only if all previous conditions are False. 
        - Must come at end of statement
        - does not require condition
        - optional
        - cannot stand alone
        - only 1 else
#elif - {if-elif-else} Asks a follow-up question, Only runs if previous conditions were false.
        - Only comes after 'if'
        - allowed to have multiple 'elif'
        - needs codition
        - cannot stand alone
        - optional
    
                              Loops
----------Types:
#For -
#While -

----------Control:
#break -
#pass -
#continue -
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


'''                                    Loops'''