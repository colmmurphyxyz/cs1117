# 13/10/21 bugs.py
# Colm Murphy 1214356486

"""
    No ending comment on line 9
"""

# I'm a comment
''' I'm a comment '''
''' I'm a comment '''
""" I'm a comment """
age = 7 # I'm a comment

# no parameter titled `a_parameter`
def a_function(a_parameter):
    return a_parameter

# no colon after `def a_function():`
def a_function():
    return "a_parameter"

# no error
def a_function(a_parameter) :
    return a_parameter

# no comma between `a_parameter` and `a_second_parameter`
def a_function(a_parameter, a_second_parameter):
    return a_parameter

# no variable called `a_second_parameter`
print(a_second_parameter)

# no comma in return statement
def a_function(a_parameter, a_second_parameter):
    return a_parameter, a_second_parameter