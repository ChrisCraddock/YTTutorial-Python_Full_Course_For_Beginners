'''                                            Parameters vs Global vs Local Variables
|What determines the Type:
|                   - How long they live
|                   - Who can access them
|                   - Accepts 1 Input and gives 1 Output
|                   - Accepts many Input and gives many Output
|===================================================================================================================|
|Parameters
|                   - The value that goes in through an Input
|                   - Names used in function definition that describe what data the function expects
|def function_name(Parameter):
|       <line of code>-----
|       <line of code>     |<--Body
|       <line of code>-----
|
|function_name(Argument)
|===================================================================================================================|
|Global:
|                   - Created outside the function
|                   - Can be accessed anywhere
|                   - Ex: Global = 2
|===================================================================================================================|
|Local:
|                   - Created inside the function
|                   - Can be accessed only inside the function
|                   - Ex: y
|def function_name(x):
|       Local = x * Global
|       print(Local)
|
|function_name(Argument)
|===================================================================================================================|
'''
def clean_name(x):
    cleaned = x.strip().lower()
    print('Input text:',x)
    print('Cleaned text:',cleaned)

name = ' OlIVer  '
clean_name(name)

case_rule = 'lower'
def clean_name(x):
    cleaned = x.strip()
    if case_rule == 'lower':
        cleaned = cleaned.lower()
    print('Cleaned text:',cleaned)

clean_name(name)