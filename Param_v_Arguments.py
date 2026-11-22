'''                                            Parameters vs Arguments
|Function Types:
|                   - Accepts No Inputs
|                   - Accepts Only Inputs
|                   - Accepts 1 Input and gives 1 Output
|                   - Accepts many Input and gives many Output
|===================================================================================================================|
|Parameters
|                   - The value that goes in through an Input
|                   - Names used in function definition that describe what data the function expects
|===================================================================================================================|
|Arguments
|                   - The value that goes in through an Input
|                   - Actual values passed in a function call that are assigned to Parameters
|===================================================================================================================|
|
|def function_name(Parameter):
|       <line of code>-----
|       <line of code>     |<--Body
|       <line of code>-----
|
|function_name(Argument)
|===================================================================================================================|
|Rules:
|                   - Normalize Strings
|                   - Hardcoded Value Issue: NOT reusable because it always cleans the same value
|===================================================================================================================|
'''
name = ' MariA '
def clean_text(x):
    print(x.strip().lower())

clean_text(name)