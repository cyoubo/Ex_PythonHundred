# -*- coding:UTF-8 -*-
# 需要导入math包

import math

for i in range(0, 100000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if x * x == i + 100 and y * y == i + 268:
        print i
