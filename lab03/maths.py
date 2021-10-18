# maths.py
# Colm Murphy
# 121356486

import math

""" a
Work out how many seconds there is in 42 minutes and 42 seconds?
"""
def to_seconds(minutes, seconds):
    return (int(minutes) * 60) + int(seconds)


""" b
How many miles are there in 10km? Hint there are 1.61km in 1 miles
"""
def km_to_miles(km):
    return float(km) / 1.61


""" c
If you run a 10km race in 42m 42s, what is your average pace i.e. time per
mile in minutes and seconds? 
"""
def average_pace(distance_km, time_minutes, time_seconds):
    distance = km_to_miles(distance_km)
    total_seconds = float(to_seconds(time_minutes, time_seconds))
    seconds_per_mile = total_seconds / float(distance)

    minutes_per_mile = math.floor(seconds_per_mile / 60)
    remaining_seconds = seconds_per_mile % 60
    print("average pace was %d minutes and %s seconds per mile" % (minutes_per_mile, remaining_seconds))


""" d
What is your average speed in miles per hour from item 3 above?
"""
def average_speed_mph(distance_km, time_minutes, time_seconds):
    distance = km_to_miles(distance_km)
    total_hours = float(to_seconds(time_minutes, time_seconds)) / 3600
    miles_per_hour = distance / total_hours

    print("average speed was %f miles per hour" % miles_per_hour)


def main():
    average_pace(10, 42, 42)
    average_speed_mph(10, 42, 42)


if __name__ == "__main__":
    main()


