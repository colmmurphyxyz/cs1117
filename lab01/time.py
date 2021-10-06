# time.py
# Colm Murphy 121356486

user_input = input("Enter minutes watching TV: ")
minutes_watching_tv = int(user_input)
hours = minutes_watching_tv / 60
minutes = minutes_watching_tv % 60

print("There were %d hours and %d min(s) watching TV" % (hours, minutes))
