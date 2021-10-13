# what_is_my_type.py
# Colm Murphy 121356486

variable = (1, 2, 3, 4, 5, 6, "abc", 2.3, ("one", "two", "three"))


def variable_info(var):
    """
    Takes a variable as a parameter and returns information on that variable
    :param variable: Any variable
    :return: a size-3 tuple containing the variable parameter, the variable's type and the unique id of the variable
    """
    return var, type(var), id(var)


print("The variable value was \"%s\" and its type was %s and this object has an id() of %d" % variable_info(variable))
