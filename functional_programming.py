#!/usr/bin/python3
# -*- coding = UTF-8 -*-

# Topic: 函数式编程

# ------ 返回函数，闭包 ------
# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数
# 和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”
def lazy_sum(*arg):  # 带*的为可变参数，两个*为关键字参数，用法参考LXF教程
    def sum():
        s = 0
        for a in arg:
            s = s + a
        return s
    return sum

f = lazy_sum(1,2,3,4,5)
print(f)  # 返回求和函数 <function lazy_sum.<locals>.sum at 0x101c6ed90>
print(f())  # 返回真正的函数值 15


# ------ 装饰器 ------

# 跳过暂时




# ------ 偏函数 ------

# 跳过暂时
