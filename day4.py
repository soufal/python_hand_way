#判断素数：只能被1和自身整除的数
import math

num = int(input())

for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
        print("这个数不是素数！")
        break
else:
    print("这个数是素数！")

#最后的这一个else不是同if配对的，而是和for配对的，当完成整个for循环后，将会运行这个else中的内容。
