#20Functions and Files

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

'''
seek（）移动文件读取指针到指定位置。处理的是字节，不是行。
fileObject.seek(offset[, whence])
offset---开始的偏移量，也就是代表需要移动偏移的字节数。
whence：可选，默认为0，给offset参数一个定义，0也就是从文件的开头开始算起。
1代表从当前位置开始算起，2代表从文件末尾开始算起。
可以让文件在往后读取行时，返回到任意位置读取。
'''
def rewind(f):
    f.seek( 0)


'''
readline()代表读取文件的一行，读完后将读头放到文件末尾\n后，
最后会返回一个\n,因此在结果中会发现读每一行后都换了一行。
不需要换行就在print中加一个end即可。
'''
def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

'''
此处如果不让文件读取的指针移回到文件开头，
也就是0的位置，接下来的读取每一行的操作将会读取不到任何数据
'''
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

#rewind(current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)