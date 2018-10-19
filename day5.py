#将上一课的程序改写成函数形式，
#任意写一个List作为函数的参数
#评断List中的每个元素是否为素数
#并将是素数的元素打印为字典
import math


def is_prime(arr):
    prime_dict = {'素数':[]}
    for num in arr:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            print(f"这个数{num}是素数！")
            prime_dict['素数'].append(num)
    print(f"素数字典为: {prime_dict}")
#最后的这一个else不是同if配对的，而是和for配对的，当完成整个for循环后，将会运行这个else中的内容。

arr = map(int, input().split(' '))
is_prime(arr)