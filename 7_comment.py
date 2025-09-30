# This is single line comment
'''
This is multi line comment
where there multiple lines are available
This will ignored by interpreter
'''
"""This is Document string"""



# Printing anything with single line comment
print("Hello World") # Output will be Hello World

# Multiline Comment
'''
Print Hello World
print any integer number you want
print the value of pi
'''
print("Hello World") # Output: Hello World
print(23)            # Output: 23
print(3.1416)        # Output: 3.1416



def add(a,b):
    '''
    This is add function. 
    It will take 2 numbers (int or float)
    And return the summation of the given two numbers
    '''
    return a+b

print(add.__doc__)