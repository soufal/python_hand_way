class A():
    def go(self):
        print ("go A go!")
    def stop(self):
        print ("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")
class B(A):
    def go(self):
        super(B, self).go()
        print ("go B go!")
class C(A):
    def go(self):
        super(C, self).go()
        print ("go C go!")
    def stop(self):
        super(C, self).stop()
        print ("stop C stop!")
class D(B,C):
    def go(self):
        super(D, self).go()
        print ("go D go!")
    def stop(self):
        super(D, self).stop()
        print ("stop D stop!")
    def pause(self):
        print ("wait D wait!")
class E(B,C):
    pass
a = A()
b = B()
c = C()
d = D()
e = E()
# 说明下列代码的输出结果
a.go()
#go A go!
print('--------')
b.go()
#go A go!
#go B go!
print('--------')
c.go()
#go A go!
#go C go!
print('--------')
d.go()
#当代码执行到super实例化后，
#先去找同级父类，若没有其余父类，再执行自身父类，再往下走，
#go A go!
#go C go!
#go B go!
#go D go!
print('--------')
e.go()
#go A go!
#go C go!
#go B go!
print('--------')
a.stop()
#stop A stop!
print('--------')
b.stop()
#stop A stop!
print('--------')
c.stop()
#stop A stop!
#stop C stop!
print('--------')
d.stop()
#stop A stop!
#stop C stop!
#stop D stop!
print('--------')
e.stop()
#stop A stop!
#stop C stop!
print(D.mro())
#生成method resolution order列表
#a.pause()
#Exception("Not Implemented")
#b.pause()
#Exception("Not Implemented")
#c.pause()
#Exception("Not Implemented")
d.pause()
#wait D wait!
#e.pause()
#Exception("Not Implemented")