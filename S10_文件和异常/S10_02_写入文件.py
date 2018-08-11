"""
写入空文件

    with open(file_name, 'w') as file_object:
    file_object.write("I love python programming.")


注:  'w' 表示以 写入模式 打开这个文件.
     'r' 表示以 只读模式 打开文件(不显式传递则默认采用此模式)
     'a' 表示 附加模式
     'r+' 读取和写入文件模式

若要写入的文件不存在, open()将自动创建.
若文件已存在, Python返回文件对象前清空该文件. (覆盖内容)

"""


# 'w'模式 写入文件
file_name = 'programming.txt'
with open(file_name, 'w') as file_object:

    # write()不会在文本末尾自动换行
    file_object.write('I love python programming.\n' * 2)


# 'a'模式 附加文件
file_name = 'programming.txt'
with open(file_name, 'a') as file_object:
    file_object.write('I also love artificial intelligence.\n')
    file_object.write("I'll be an expert in machine learning.\n")
