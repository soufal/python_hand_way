#Reading and Writing Files
#close:关闭文件
#read:读取文件文本
#readline:只读文件的一行
#truncate:清空文件
#write('stuff'):把‘stuff’写入文件
#seek(0):把读写位置移到文件的开头

#若不存在文件。会自动创建一个新的文件
from sys import argv

script, filename = argv
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

print("Now we will open the new file.")
print("The new file is:")
new_file = open(filename)
print(new_file.read())
new_file.close()