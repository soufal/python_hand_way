#Inheritance versus Composition
#继承和组合
#继承的大多数用法可以简化或用组合替换，并且应该不惜一切代价避免多重继承。
#子类和父类交互的三种方式：
##对孩子的行为意味着对父母的行为。
##子类上的操作覆盖父类上的操作。
##对子类的操作改变了对父类的操作   

#隐式继承  
##在父级中定义函数而不是子级中时发生的隐式操作。
print("This is implicit inheritance example!")
class Parent(object):
    def implicit(self):
        print("PARENT implicit()")
    
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print("---------------------------")

#Override Explicitly显示重写
##覆盖
print("This is Override Explicitly example!")
class Parent1(object):
    def override(self):
        print("PARENT1 override()")
    
class Child1(Parent1):
    def override(self):
        print("CHILD1 override()")

dad1 = Parent1()
son1 = Child1()

dad1.override()
son1.override()

print("---------------------------")

#Alter Before or After
##使用super函数来获取希望调用的parent
print("This is Alter Before or After example!")

class Parent2(object):
    def altered(self):
        print("PARENT2 altered()")

class Child2(Parent2):
    def altered(self):
        print("CHILD2 altered()")
        super(Child2, self).altered()
        print("CHILD, AFTER PARENT2 altered()")

dad2 = Parent2()
son2 = Child2()

dad2.altered()
son2.altered()

print("---------------------------")
#Multiple inheritance
##多重继承是指定义一个从一个或多个类继承的类

print("This is Composition example!")
##不使用父类，而是直接调用同级类的方法 chirld has-a other 关系

class Other(object):
    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")

class Child3(object):
    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD. AFTER OTHER altered()")

son3 = Child3()
son3.implicit()
son3.override()
son3.altered()