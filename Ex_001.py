# -*- coding:UTF-8 -*-

# 独立编写版
elements = (1, 2, 3, 4)
result = []

for i in range(0, 4):
    x = elements[i]*100
    for j in range(0, 4):
        if j != i:
            y = elements[j]*10
            for k in range(0, 4):
                if k != j and k != i:
                    z = elements[k]
                    result.append(x+y+z)

print result

# 建议代码版
elements = (1, 2, 3, 4)
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            if i != j and j != k and k != i:
                print elements[i], elements[j], elements[k]

