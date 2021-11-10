# ScriptName: main.py
# Author: Colm Murphy

# template for calling functions in another file

# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print(add_to_list_no_sort(5, [1, 3, 7, 9]))
    print(add_to_list_no_sort(10, [1, 3, 7, 9]))
    print(add_to_list_no_sort("c", ["a", "b", "d", "e"]))
    print(add_to_list_no_sort(5, [1, 5, 7, 9]))
    print(add_to_list_no_sort(5))
    print(add_to_list_no_sort(5, ["a", "b", "d", "e"]))
    print(add_to_list_no_sort(5, 5))
    print(add_to_list_no_sort(99, ["a", "b", "d", "e"]))
    print(add_to_list_no_sort(99.5, ["a", "b", "d", "e"]))


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
