#装饰器例子学习
import logging
from functools import wraps

#原代码
def use_logging(func):
    logging.warn("%s is running" % func.__name__)
    func()

def bar():
    print('i am bar')

use_logging(bar)


#加了装饰器@log后
def log(func):
    def wrapper(*arg, **argv):
        logging.warn("%s is running" % func.__name__)
        return func(*arg, **argv)
    return wrapper

@log
def bar():
    print('i am bar')

bar()


#带参数的装饰器
def loging(level):
    def decorator(func):
        def wrappr(*arg, **kwarg):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            return func(*arg)
        return wrappr
    return decorator

@loging("warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()


#类装饰器
class Foo(object):
    def __init__(self, func):
        self._func = func
    
    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')

@Foo
def bar():
    print('bar')

bar()

#此时函数f被with_logging取代了，他的相关信息，例如参数等变成了with_logging函数的信息了

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
    return x + x * x

#print("The result is: ", f(2))

#使用wraps来将原函数的元信息拷贝到装饰器函数中
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f1(x):
    return x + x * x
#f1(3)
print("The result is: ", f1(2))