#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#python继承顺序遵循C3算法，只要在一个地方找到了所需的内容，就不再继续查找
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A,B):
    pass

class C2(A,B):
    def bar(self):
        #super(C2, self).bar()
        print('C2-bar')

class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()


class NewStyleClassA(object):
    var = 'New Style Class A'


class NewStyleClassB(NewStyleClassA):
    pass


class NewStyleClassC(object):
    var = 'New Style Class C'


class SubNewStyleClass(NewStyleClassB, NewStyleClassC):
    pass


if __name__ == '__main__':
    print(SubNewStyleClass.mro())
    print(SubNewStyleClass.var)