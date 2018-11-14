# -*- coding:UTF-8 -*-

import time

myDict = {"A": 12, "B": 33}

# 字段方法，将字典元素转换为key-value元组
for key, value in myDict.items():
    print key, value
    time.sleep(1)
