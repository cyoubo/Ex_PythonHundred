# -*- coding:UTF-8 -*-

# 独立编写版
elements = (1, 2, 3, 4)
result = []

for i in range(0, 4):
    x = elements[i]*100
    for j in range(0, 4):
        if j == i:
            continue
        else:
            y = elements[j]*10
            for k in range(0, 4):
                if k == j or k == i:
                    continue
                else:
                    z = elements[k]
                    result.append(x+y+z)

print result