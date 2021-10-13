# 13/10/21 time.py
# Colm Murphy 121356486

user_input = input("Enter minutes watching TV: ")
minutes_watching_tv = int(user_input)
# hours = minutes_watching_tv / 60
# minutes = minutes_watching_tv % 60


def minutes_to_hours(minutes):
    """
    :param minutes: Total minutes spent watching TV
    :return: Tuple of size 2 representing the hours and minutes spent watching TV
    """
    return (minutes // 60, minutes % 60)


print("There were %d hours and %d min(s) watching TV" % minutes_to_hours(minutes_watching_tv))
