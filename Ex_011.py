# -*- coding:UTF-8 -*-


def fab(a):
    if a == 0 or a == 1:
        return 1
    else:
        return fab(a - 2) + fab(a - 1)


month = int(raw_input("input month："))

for i in range(0, month):
    print "month %d count %d" % (i + 1, fab(i))



