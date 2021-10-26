# ScriptName: my_functions.py
# Author: Colm Murphy
# 121356486

import math

def print_function():
    print("I'm in another file :)")


def seperated_input(param1, param2, sepr=" ", endr="\n"):
    print(param1, param2, sep=sepr, end=endr)


def three_numbers(num1, num2, num3):
    return num1 == num2 and num2 == num3


def test_three_numbers():
    all_tests_passed = True
    if not three_numbers(3, 3, 3):
        all_tests_passed = False
        print("Failed test 1")
    if three_numbers(3, 2, 3):
        all_tests_passed = False
        print("Failes test 2")
    if three_numbers(3, "a", 3):
        all_tests_passed = False
        print("Failed Test 3")
    if all_tests_passed:
        print("All tests passed")


def seasons(num):
    if not type(num) == type(5):
        return "Input value must be a number"
    if num == 1:
        return "Winter"
    elif num == 2:
        return "Spring"
    elif num == 3:
        return "Summer"
    elif num == 4:
        return "Autumn"
    else:
        return "Number entered, %d, is out of bounds" % num

def grades(num):
    if type(num) != type(5):
        return "Input value must be a number"
    if 0 <= num <= 24:
        return "F"
    elif 25 <= num <= 39:
        return "E"
    elif 40 <= num <= 54:
        return "D"
    elif 55 <= num <= 69:
        return "C"
    elif 70 <= num <= 84:
        return "B"
    elif 85 <= num <= 100:
        return "A"
    else:
        return "X"

def equal_numbers(num1, num2):
    # if the input values are not integers or floats, return an error message
    if (type(num1) != type(5) and type(num2) != type(5.0)) or (type(num2) != type(5) and type(num2) != type(5.0)):
        return "Input value(s) must be a number"
    if num1 == num2:
        return math.sqrt(float(num1))
    else:
        return num1 ** 2, num2 ** 2
