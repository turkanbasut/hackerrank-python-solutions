# Task
#
# You are given a date. Your task is to find what the day is on that date.
#
# Input Format
#
# A single line of input containing the space separated month, day and year,
# respectively, in MM / DD / YYYY  format.


import calendar

m, d, y = map(int, input().strip().split())

print(calendar.day_name[calendar.weekday(y, m, d)].upper())