# bugs.py
# Colm Murphy
# 121356486

from my_functions import *

# Are there bugs here?
# no import statement at the top of the file
# wrong paramater names, `my_sep` and `my_end` instead of `sepr` and `endr`
seperated_input("A", "B", sepr=" and ", endr=" and C\n")
seperated_input("A", "B", endr=" and C\n", sepr=" and ")
# parameters in the wrong order
seperated_input("A", endr=" and C\n", sepr=" and ", param2="B")
seperated_input("A", "B", sepr=" and ")
seperated_input("A", "B", endr=" and C\n")
# too many paramaters
seperated_input("A", "B", sepr=" and ", endr=" and C\n")
seperated_input("8", "7", sepr=" + ", endr=" = 15\n")
# no quotation marks around `+`
seperated_input(8, 7, sepr="+", endr=" = 15\n")
# endr should be a string type
seperated_input(8, 7, sepr=" + ", endr=15)
seperated_input(8, 7, sepr=" + ", endr=" = 15"+"\n")
