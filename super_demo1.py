class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        print(f"m is {m}")
        #这里使用的n是D中__init__的n，不是A的n
        #因为D只继承了A中的add方法，自己的__init__属性覆盖了A的
        print(f"n is {self.n}")
        self.n += m
        print(f"A:{self.n}")


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        print('newb')
        self.n += 3
        print(f"B:{self.n}")


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        print('newc')
        self.n += 4
        print(f"C:{self.n}")

class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print(f"m is {m}")
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5
        print(f"D:{self.n}")


d = D()
d.add(2)
#self is <__main__.D object at 0x7f133a2136d8> @D.add
#self is <__main__.D object at 0x7f133a2136d8> @B.add
#self is <__main__.D object at 0x7f133a2136d8> @C.add
#self is <__main__.D object at 0x7f133a2136d8> @A.add
#newc
#newb

print(d.n)
#19