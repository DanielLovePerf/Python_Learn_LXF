#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Topic: 面向对象的编程

"""特性
静态语言 vs 动态语言:
1. 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则
，将无法调用run()方法
2. 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就
可以了
"""

# ------- 多态 -------
"""多态：
1. 新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可
以不加修改地正常运行，原因就在于多态
2. 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat
、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可新增一个Animal的子类，不必对run_twice()做任
何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
3. 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat
、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可
"""

# E.g.

class Animal(object):
    def run(self):
        print("Animal is running")
    def runTwice(aa):  # runTwice(aa)可以写在类外边，通过传入对象参数调用
        aa.run()

class Dog(Animal):
    def run(self):
        print("Dog is running")

class Cat(Animal):
    def run(self):
        print("Cat is running")

a = Animal()
a.run()
a.runTwice() # Animal is running
d = Dog()
d.run()
d.runTwice()  # dog is running
c = Cat()
c.run()
c.runTwice()  # cat is running

"""
a = Animal()
d = Dog()
c = Cat()
run_twice写在里边，调用是：
a.run_twice()
d.run_twice()
c.run_twice()
run_twice写在外边，调用是：
run_twice(a)
run_twice(b)
run_twice(c)

不管run_twice在类里边还是外边，继承或者鸭子特性都是通过run方法体现的
不过，run_twice写在里边，与run方法一样，体现了继承和鸭子特性。

"""
# ------- 获取对象属性 -------

# 判断对象类型,用type(),  notes: a = Animal()
print(type(a)) # <class '__main__.Animal'>
print(type('123'))  # <class 'str'>

# 判断一个对象是否是函数
import types
print(type(a) == types.FunctionType) # False
def fn():
    pass
print(type(fn) == types.FunctionType) # True

# 对于class的继承关系来说，使用type()就很不方便,可以使用isinstance()函数
print(isinstance(d,Animal))  # True,  dog继承与Animal

# dir()
print(dir(Animal))   # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__'

# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len('ABC'))
print('ABC'.__len__())


# 演示类的属性和实例属性
class Student(object):
    name = 'Student'

s = Student() # 创建实例s

print(s.name) # 输出Student： 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name) # 输出Student， 打印类的name属性

s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 输出Michael： 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性

print(Student.name) # 输出Student： 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name) # 输出Student： 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了



