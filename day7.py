#利用装饰器给之前课程所写的判断素数的程序增加一个「有趣的」功能。
import math, time

def com_time(func):
    def wrapper(*arg, **argv):
        start_time = time.time()
        result = func(*arg, **argv)
        end_time = time.time()
        print("The run time is: ", start_time - end_time)
        return result
    return wrapper

def log(func):
    def wrapper(*arg, **argv):
        print("初始数组为： ", *arg)
        print("其长度为： ", len(*arg))
        return func(*arg, **argv)
    return wrapper

@com_time
@log
def is_prime(arr):
    arr = map(int, arr)
    prime_dict = {'素数':[]}
    for num in arr:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            prime_dict['素数'].append(num)
    return prime_dict
    
#最后的这一个else不是同if配对的，而是和for配对的，当完成整个for循环后，将会运行这个else中的内容。

arr = input().split(' ')
final = is_prime(arr)
print(f"素数字典为: {final}")