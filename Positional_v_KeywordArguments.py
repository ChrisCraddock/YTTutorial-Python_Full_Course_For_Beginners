'''                                            Positional vs Keyword Arguments
|Rules:
|                   - Number of arguments must match the number of parameters
|                   - Positional: The order of Args must match the order of the Parameters
|                   - Keyword: The names of Args must match the names of the Parameters
|===================================================================================================================|
|Positional Arguments:
|                   - Values pass to the function based on their Order
|                   - Order matters if output matters
|                   - Faster than typing exact names
|===================================================================================================================|
|Keyword Arguments:
|                   - Values pass to the function based on their Names
|                   - Safer to use if mixing order
|                   - More overhead and chanes to parameter naming has to be reflected for every use
|===================================================================================================================|
|Mixed Arguments Rules:
|                   - Can not start with keyword argument
|                   - Can not alternate between after 1st instance of keyword
|                   - Don't mix if possible 
|===================================================================================================================|
|Default Parameter:
|                   - Parameter that already has a value so if you don't pass anything Python uses that value automatically
|                       -Ex: def clean_name(first_name,last_name, country='n/a'):
|                   - Parameters without a default must come before those with a default
|===================================================================================================================|
'''
#Building a full clean name
def clean_name(first_name,last_name):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first+' '+last
    print(full_name)

firstName = ' StEVE  '
lastName = 'McsTeeven  '

clean_name(firstName,lastName) #Position Arg
clean_name(first_name= ' StEVE  ', last_name = 'McsTeeven  ') #Keyword Arg