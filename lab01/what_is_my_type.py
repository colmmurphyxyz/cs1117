# what_is_my_type.py
# Colm Murphy 121356486

variable = (1, 2, 3, 4, 5, 6, "abc", 2.3, ("one", "two", "three"))
variable_type = type(variable)

print("The variable value was \"%s\" and its type was %s" % (variable, variable_type))