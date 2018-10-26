#Strings, bytes, and character encodings

import sys
script, input_encoding, error = sys.argv

#这里使用一个递归来读取文件的每一行
def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    #使用strip（）去除字符串末尾的\n
    next_lang = line.strip()
    #使用utf-8对字符串进行编码,errors默认为 'strict',意为编码错误引起一个UnicodeError。
    #encode：字符串到bytes decode：bytes到字符串Decode Bytes, Encode Strings
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)