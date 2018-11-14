# -*- coding:UTF-8 -*-


def fab(a):
    # type: (object) -> object
    if a == 1 or a == 2:
        return 1
    else:
        return fab(a - 2) + fab(a - 1)


print fab(10)
