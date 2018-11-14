# -*- coding:UTF-8 -*-

a = [1, 2, 3]

c = a[:]  # 浅拷贝：a,c指向不同内存空间
c[1] = 15  # c的修改不对a有影响

print a

b = a  # 浅拷贝：a,b指向同一个内存空间
b[1] = 5  # b的修改a造成影响

print a

