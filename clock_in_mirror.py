from random import randint
import re

def rand_time():
    return "{:02}:{:02}".format(randint(1, 12), randint(0, 59))
# Test.assert_equals(what_is_the_time("06:35"), "05:25", "didn't work for '06:35'")
# Test.assert_equals(what_is_the_time("11:59"), "12:01", "didn't work for '11:59'")
# Test.assert_equals(what_is_the_time("12:02"), "11:58", "didn't work for '12:02'")
# Test.assert_equals(what_is_the_time("04:00"), "08:00", "didn't work for '04:00'")
# Test.assert_equals(what_is_the_time("06:00"), "06:00", "didn't work for '06:00'")
# Test.assert_equals(what_is_the_time("12:00"), "12:00", "didn't work for '12:00'")

# Begin
hours = {}
inv_h = 11
for h in range(1, 13):
    hours[h] = inv_h
    inv_h -= 1
hours[12] = 12

hours_mid = {}
inv_h = 10
for h in range(1, 12):
    hours_mid[h] = inv_h
    inv_h -= 1
hours_mid[11] = 12
hours_mid[12] = 11

minutes = {}
inv_m = 59
for m in range(1, 60):
    minutes[m] = inv_m
    inv_m -= 1
minutes[0] = 0


def what_is_the_time(time_in_mirror):
    time = re.split(r':', time_in_mirror)
    if time[1] == '00':
        mirror_hour = hours.get(int(time[0]))
    else:
        mirror_hour = hours_mid.get(int(time[0]))
    mirror_min = minutes.get(int(time[1]))
    return "{:02}:{:02}".format(mirror_hour, mirror_min)

print(what_is_the_time("06:35"))