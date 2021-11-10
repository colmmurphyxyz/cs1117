# ScriptName: my_functions.py
# Author: Colm Murphy
# Student Number: 121356486

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


def seasons(number):
    seasons = ("Winter", "Spring", "Summer", "Autumn")
    if type(number) != int:
        return "Input value must be a number"
    if number < 1 or number > 4:
        return "Number entered, %d, is outside of input values" % number
    return seasons[number - 1]


def slice_reverse(input_value):
    try:
        if type(input_value) == tuple or type(input_value) == list:
            # convert tuple/list into a string
            input_string = ""
            x = 0
            while x < len(input_value):
                input_string += str(input_value[x])
                x += 1
            input_value = input_string
        else:
            input_value = str(input_value)
    except ValueError:
        return "Input value must be a String"
    x = 0
    y = len(input_value) - 1
    while y > x:
        if input_value[x] != input_value[y]:
            return False
        x += 1
        y -= 1
    return True


def add_to_list(value, list = []):
    if type(list) != type([1]):
        return "Incorrect value defined for param list"
    try:
        if value in list:
            return list
        list.append(value)
        return sorted(list)
    except TypeError:
        return "sort() does not like this mixture of elements"


def add_to_list_no_sort(value, list: list = []):
    # helper function for comparing numbers and characters
    def f(x):
        if type(x) == str:
            return ord(x)
        else:
            return x

    if type(list) != type([1]):
        return "Incorrect value defined for param list"
    if len(list) == 0:
        return [value]

    i = 0
    try:
        while i < len(list):
            if f(value) < f(list[i]):
                return list[0:i] + [value] + list[i:]
            elif f(value) == f(list[i]):
                return list
            i += 1
    except IndexError:
        return list
    return list + [value]

# def add_to_list_no_sort(value, list: list = []):
#     # helper function for comparing numbers and characters
#     def f(x):
#         if type(x) == str:
#             return ord(x)
#         else:
#             return x

#     if type(list) != type([1]):
#         return "Incorrect value defined for param list"
#     if len(list) == 0:
#         return [value]

#     try:
#         if f(value) < f(list[0]):
#             return [value] + list
#         elif f(value) == f(list[0]):
#             return list

#         if f(value) < f(list[1]):
#             return list[0:1] + [value] + list[1:]
#         elif f(value) == f(list[1]):
#             return list

#         if f(value) < f(list[2]):
#             return list[0:2] + [value] + list[2:]
#         elif f(value) == f(list[2]):
#             return list

#         if f(value) < f(list[3]):
#             return list[0:3] + [value] + list[3:]
#         elif f(value) == f(list[3]):
#             return list

#         # if value > the last element in the list
#         return list + [value]
#     except IndexError:
#         # if value > the last element in the list
#         return list
