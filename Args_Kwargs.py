'''                                            *Args and **Kwargs
|*Agrs/**Kwargs:
|                   - Sometimes you don't know in advance how amny arguments will be passed to your function
|                   - allow functions to accept a unknown number of arguments
|                   - * = positional | ** = keyword
|===================================================================================================================|
|*Agrs:
|                   - Class: Tuple
|                   - Use when passing similar values
|===================================================================================================================|
|Keyword Args (**Kwargs):
|                   - Class: Dictionary
|                   - Use when passing different type of values
|                   - Only works with keyword arguments
|
|===================================================================================================================|
'''
#Calc the total of values
def total(*args):
    print(sum(args))

total(1,2)
total(1,2,3)

#Create user profile
def create_user(**kwargs):
    print(kwargs)

create_user(first_name='Mo',
            last_name='Sala',
            age=33,
            country='Egypt')