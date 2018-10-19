#Reading Files
#先使用argv来得到文件名。
#再使用input来得到文件名。
from sys import argv

script, filename = argv
#打开文件
txt = open(filename)

print(f"here's your file {filename}:")
#读取文件全部内容并输出。
print(txt.read())

txt.close()
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()