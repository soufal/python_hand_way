#day6:1. 掌握链接中 Python 教程的高级特性
#2. 利用生成器生成斐波那契数列
#普通函数生成斐波拉契数列
def Fibonacci(num):
    n0, n1 = 1, 1
    for i in range(num):
        print(n0, end=" ")
        n0, n1 = n1, n0+n1
    print('\n')
Fibonacci(6)

#生成器
def Fibonacci(num):
    n0, n1 = 1, 1
    for i in range(num):
        yield(n0)
        n0, n1 = n1, n0+n1
f = Fibonacci(6)
print(f)
for i in f:
    print(i)
