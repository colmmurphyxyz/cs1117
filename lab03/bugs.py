# bugs.py
# Colm Murphy
# 121356486

'''
If I leave my house at 6:52am and run 1 mile at an easy pace (8:15 minutes [8 minutes
and 15 seconds] per mile), then 3 miles at tempo (7:12m per mile) and 1 mile at the easy
pace again, what time do I get home for breakfast?
'''
# departure time is wrong
departure_time_hours = 6
departure_time_minutes = 52
departure_time_seconds = (departure_time_hours * 3600) + (departure_time_minutes * 60)

easy_pace_mins = 8
easy_pace_secs = 15
easy_pace_total_sec = (easy_pace_mins * 60) + easy_pace_secs

faster_pace_mins = 7
faster_pace_secs = 12
# wrong variable name, should be called `faster_pace_total_sec`
faster_pace_total_sec = (faster_pace_mins * 60) + faster_pace_secs

# should add the two terms in brackets instead of multiplying
time_spent_running = (easy_pace_total_sec * 2) + (faster_pace_total_sec * 3)
print(time_spent_running)

time_return_home_total_secs = departure_time_seconds + time_spent_running

time_return_home_hours = time_return_home_total_secs // 3600
time_return_home_mins = (time_return_home_total_secs % 3600) // 60
# should replace `time_return_home_mins` with `time_return_home_total_secs`
time_return_home_secs = (time_return_home_total_secs % 3600) % 60

print(time_return_home_hours, ":",
      time_return_home_mins, ":", time_return_home_secs, "(HH:MM:SS)")
