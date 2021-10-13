# what_is_my_name.py
# Colm Murphy 121356486

def ask_for_name():
    """
    Takes a string input from the user, converts all characters in the string to lower case,
    then capitalises the first letter
    """
    return input("What is your name? ").lower().capitalize()


user_name = ask_for_name()
print(user_name)
