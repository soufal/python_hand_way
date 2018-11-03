#You make a game
#异常处理
#尝试去返回一个s的int强制类型结果
#如果出现ValueError错误则返回None
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

