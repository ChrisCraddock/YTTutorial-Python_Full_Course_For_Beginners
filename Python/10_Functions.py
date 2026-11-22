'''                                            Functions
|What is a function?
|                   - A small reusable block of code that does 1 specific job
|                   - Fast changes
|                   - Smaller code
|                   - Clean
|                   - Easy to understand and READ
|                   - Code modularity
|===================================================================================================================|
|Sources of Functions:
|                   - Built-In:
|                       - Number
|                       - String
|                       - Data Structure
|                   - Standard Library written by Python team
|                       - Import > Use
|                   - External Library written by 3rd-Party
|                       - Install > Import > Use
|                   - User-Defined
|                       - YOU write them
|===================================================================================================================|
|Golden Rule:
|                   #1 Check the Built-In Functions
|                   #2 Check Standard Libraries
|                   #3 External Library written by 3rd-Party
|                   #4 User-Defined
|===================================================================================================================|
|User-Defined Functions:
|                   - 2 parts: Function Definition & Function Call
|                       - Function Definition: def function_name():
|                       - Function Call: function_name()
|
|                   - Does not execute code inside function unless called
|===================================================================================================================|
'''
''' Function '''
def greet():
    print('Hello')
greet()

def make_coffee():
    print('Start Machine')
    print('Make Coffee')
    print('Add Milk')
    print('Enjoy it')

make_coffee()