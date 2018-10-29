#Modules, Classes, and Objects
#面向对象编程：使用类，您可以为程序添加一致性，以便以更干净的方式使用它们。

#Modules Are Like Dictionaries
mystuffs = {'apple': "I AM APPLES!"}
print(mystuffs['apple'])

#使用一个自定模块
import mystuff
mystuff.apple()
print(mystuff.tangerine)

#Class are like modules
'''
类是一种对函数和数据进行分组并将它们放在容器中的方法，
以便您可以使用（点）运算符.来访问它们。 
'''
class MyStuff(object):
    #调用该函数来初始化你新创建的空对象。
    def __init__(self):
        #tangerine是一个实体变量
        self.tangerine = "And now a thousand years between"
    #定义一个apple方法
    def apple(self):
        print("I AM CLASSY APPLES!")

#Objects are like import
#模块里称为import，类中称为“实例化(instantiate)”
#实例化一个类就得到了一个“对象”
#通过像调用函数一样调用类来实例化(创建)类
thing = MyStuff()
thing.apple()
print(thing.tangerine)

#Getting things from things

#dict style
print("This is dict style: ")
print(mystuffs['apple'])

#module style
print("This is modele style: ")
mystuff.apple()
print(mystuff.tangerine)

#class style
print("This is class style: ")
thing = MyStuff()
thing.apple()
print(thing.tangerine)
