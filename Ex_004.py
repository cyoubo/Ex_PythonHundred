# -*- coding:UTF-8 -*-

year = int(raw_input("year"))
month = int(raw_input("month"))
day = int(raw_input("day"))

monthdays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
daySum = 0

print range(0, month)

if 12 > month > 0:
    for i in range(1, month):
        daySum += monthdays[i-1]

daySum += day

if month > 2:
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 !=0)):
        daySum += 1

print daySum
