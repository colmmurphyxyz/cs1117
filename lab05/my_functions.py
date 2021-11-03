# ScriptName: my_functions.py
# Author: Colm Murphy
# Student Number: 121356586

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


def fizz_buzz_1(num1):
    try:
        if num1 % 15 == 0:
            return "FizzBuzz"
        if num1 % 3 == 0:
            return "Fizz"
        if num1 % 5 == 0:
            return "Buzz"
        return num1
    except TypeError:
        return "Input value must be a number"

def fizz_buzz(num1, divisor_1, divisor_2):
    # if type(num1) != int or type(divisor_1) == int or type(divisor_2) == int:
    #     return "Input value(s) must be a number"
    try:
        if num1 % (divisor_1 * divisor_2) == 0:
            return "FizzBuzz"
        if num1 % divisor_1 == 0:
            return "Fizz"
        if num1 % divisor_2 == 0:
            return "Buzz"
        return num1
    except TypeError:
        return "Input value(s) must be a number"


def grades(num):
    if type(num) == int:
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
            return "The input numerical grade is outside the range supported"
    elif type(num) == str:
        if num == 'A':
            return "85-100"
        elif num == 'B':
            return "70-84"
        elif num == 'C':
            return "55-69"
        elif num == 'D':
            return "40-54"
        elif num == 'E':
            return "25-39"
        elif num == "F":
            return "0-24"
        else:
            return "The input letter grade is outside the range supported"
    else:
        return "Input value must be a number or letter"
