# -*- coding:UTF-8 -*-

level = (1000000, 600000, 400000, 200000, 100000, 0)
rate = (0.01, 0.015, 0.03, 0.05, 0.075, 0.1)

x = float(raw_input("xxxx w"))

rest = 0
for i in range(0, 6):
    if x > level[i]:
        rest += level[i]*rate[i]
        print (x-level[i])*rate[i]
        x = level[i]

print rest

