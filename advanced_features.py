#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Topic: Python高级特性

# ------列表生成式------
# 两层循环
l = [m + n for m in 'XYZ' for n in 'ABC']
print(l) # ['XA', 'XB', 'XC', 'YA', 'YB', 'YC', 'ZA', 'ZB', 'ZC']

# 列出当前目录下所有文件名和目录名
import os
dirs = [d for d in os.listdir('.')]
print(dirs)

# 使用内建的isinstance函数可以判断一个变量是不是字符串
x = 123
y = '123'
print(isinstance(x, str))  # False
print(isinstance(y, str))  # True

# 可迭代对象(iterable)、迭代器(iterator)、生成器(generator)
"""
可以直接作用于for循环的数据类型有以下几种：
1. 一类是集合数据类型，如list、tuple、dict、set、str等；
2. 一类是generator，包括生成器和带yield的generator function。

可迭代对象：Iterable: 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
迭代器：Iterator:
 - 而生成器generator不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值
 - 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
"""
    
# ------生成器generator------
# 列表生成式,符号[]: 直接创建一个列表，如果只是用部分元素，浪费空间
# 生成器generator，符号(): 是边推导边计算的生成方式，生成的是迭代器，不是列表

L = [x * x for x in range(10)]
G = (x * x for x in range(10))
print(L) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(G) # <generator object <genexpr> at 0x7f8cb3fada20>
for g in G:  # 可通过for循环输出迭代器，一般不用next（）
    print(g)

from collections import Iterable
from collections import Iterator
# 判断对象是否可迭代
print(isinstance(G, Iterable)) # True
print(isinstance({}, Iterable)) # True



# ------迭代器Iterator------
"""
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数
"""

print(isinstance('abc', Iterable)) # True
print(isinstance({}, Iterable)) # True

print(isinstance('abc', Iterator)) # False
print(isinstance({}, Iterator)) # False


print(isinstance(iter('abc'), Iterator)) # True
print(isinstance(iter({}), Iterator)) # True

